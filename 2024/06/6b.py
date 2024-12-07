from lab import Lab
from copy import deepcopy
from rich.progress import track
from concurrent.futures import ProcessPoolExecutor, as_completed


def path_is_looped(lab: Lab):
    for turn in lab.turn_points:
        if lab.turn_points.count(turn) > 1:
            return True
    return False


def check_lab(lab: Lab):
    while not lab.guard_left:
        turned = lab.move_guard()
        if turned and path_is_looped(lab):
            return True
    return False


def get_new_lab(lab: Lab, guard_path: list[tuple[int, int]]):
    for r in range(len(lab.grid)):
        for c in range(len(lab.grid[0])):
            # Skip spaces the guard won't interact with
            if (r, c) not in guard_path:
                continue

            new_lab = deepcopy(lab)
            if (r, c) != new_lab.guard and lab.grid[r][c] == 0:
                new_lab.grid[r][c] = 1
                yield new_lab


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    lab = Lab(lines)
    while not lab.guard_left:
        lab.move_guard()

    count = 0
    labs = list(get_new_lab(Lab(lines), lab.guard_path))
    results = []
    with ProcessPoolExecutor() as e:
        futures = [e.submit(check_lab, lab) for lab in labs]
        for future in track(as_completed(futures), total=len(labs)):
            if future.result():
                count += 1
    print(count)
