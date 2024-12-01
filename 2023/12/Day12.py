import itertools
import concurrent.futures as cf
from tqdm import tqdm


def check_arrangement(arr, groups):
    current_group_size = 0
    group_sizes = []
    for i in range(len(arr)):
        if arr[i] == '#':
            current_group_size += 1
        else:
            if current_group_size > 0:
                group_sizes.append(current_group_size)
                current_group_size = 0
    if current_group_size > 0:
        group_sizes.append(current_group_size)

    if group_sizes == groups:
        return True
    else:
        return False


def count(line, debug=False):
    unknown = line.split(' ')[0]
    groups = [int(i) for i in line.split(' ')[1].split(',')]
    if debug:
        print(unknown, groups)

    valid_arrangements = 0
    question_indicies = [i for i in range(len(unknown)) if unknown[i] == '?']
    for i in range(len(question_indicies)+1):
        for c in itertools.combinations(question_indicies, i):
            a = list(unknown)
            for i in c:
                a[i] = '#'

            arrangement = ''.join(a)
            if check_arrangement(arrangement, groups):
                valid_arrangements += 1
    return valid_arrangements


if __name__ == '__main__':
    unfolded_lines = []
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            springs, groups = line.strip().split(' ')
            new_line = '?'.join([springs] * 5) + ' ' + ','.join([groups] * 5)
            unfolded_lines.append(new_line)

    print(len(unfolded_lines))

    with cf.ProcessPoolExecutor(32) as executor:
        with tqdm(total=len(unfolded_lines)) as pbar:
            c = 0
            for future in executor.map(count, unfolded_lines):
                c += future
                pbar.update(1)
            print(c)