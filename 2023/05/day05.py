from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm
from multiprocessing import cpu_count

def process_map(maps, map_name, input_val):
    map_ = maps[map_name]
    for range_ in map_:
        if input_val >= range_[1] and input_val <= range_[1] + range_[2] - 1:
            offset = input_val - range_[1]
            return range_[0] + offset
    return input_val


def get_seed_location(maps, seed_num):
    # print(f'Processing seed {seed_num}')
    x = seed_num
    for map_name in maps:
        from_name, to_name = map_name.split('-')[0], map_name.split('-')[-1]
        pre_x = x
        x = process_map(maps, map_name, x)
        # print(f'\t{from_name} -> {to_name}: {pre_x} -> {x}')
    return x


def process_subrange(maps, range_, use_tqdm=False):
    start, stop = range_
    min_loc = None
    if use_tqdm:
        with tqdm(total=stop-start) as pbar:
            for seed_num in range(start, stop):
                loc = get_seed_location(maps, seed_num)
                if min_loc is None or loc < min_loc:
                    min_loc = loc
                pbar.update(1)
    else:
        for seed_num in range(start, stop):
            loc = get_seed_location(maps, seed_num)
            if min_loc is None or loc < min_loc:
                min_loc = loc
    return min_loc


def process_range(maps, range_):
    start, stop = range_
    cpus = cpu_count()

    # Create cpu count ranges of equal size, dividing from range_
    ranges = []
    range_size = (stop - start) // cpus
    for i in range(cpus):
        ranges.append((start + i * range_size, start + (i+1) * range_size))
    ranges[-1] = (ranges[-1][0], stop)

    use_tqdm = [True] + [False] * (cpus - 1)

    min_loc = None
    with ProcessPoolExecutor() as executor:
        futures = {executor.submit(process_subrange, maps, ranges[i], use_tqdm[i]): ranges[i] for i in range(cpus)}
        for future in as_completed(futures):
            if min_loc is None or future.result() < min_loc:
                min_loc = future.result()

    return min_loc


if __name__ == '__main__':
    # === PART 1 === #
    seeds = []
    maps = {}
    with open('input.txt') as f:
        data = f.readlines()

        seeds = [int(x) for x in data[0][7:].split(' ')]

        current_map = []
        current_map_name = ''
        for line in data[2:]:
            if line[0].isalpha():
                current_map_name = line.split(' ')[0]
            elif line[0].isdigit():
                current_map.append([int(x) for x in line.split(' ')])
            else:
                maps[current_map_name] = current_map
                current_map_name = ''
                current_map = []
        maps[current_map_name] = current_map

    min_loc = None
    for seed_num in seeds:
        loc = get_seed_location(maps, seed_num)
        if min_loc is None or loc < min_loc:
            min_loc = loc
    print('Part 1:', min_loc)

    # === PART 2 === #
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        start = seeds[i]
        stop = seeds[i] + seeds[i+1]
        seed_ranges.append((start, stop))

    min_loc = None
    for r in seed_ranges:
        loc = process_range(maps, r)
        if min_loc is None or loc < min_loc:
            min_loc = loc
    print('overal min', min_loc)