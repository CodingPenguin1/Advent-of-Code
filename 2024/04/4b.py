import numpy as np


def check_bounds(arr, r, c, r_end=0, c_end=0):
    return 0 <= r < len(arr) and 0 <= r_end <= len(arr) and 0 <= c < len(arr[0]) and 0 <= c_end <= len(arr[0])


def check_block(arr: np.array, r: int, c: int):
    mas = list("MAS")
    mas_rev = list(reversed("MAS"))

    block = arr[r : r + 3, c : c + 3]
    rotated_block = np.rot90(block)
    diag = list(np.diag(block))
    rot_diag = list(np.diag(rotated_block))

    return (diag == mas or diag == mas_rev) and (rot_diag == mas or rot_diag == mas_rev)


def find_xmas(arr: np.array):
    count = 0
    for r in range(len(arr) - 2):
        for c in range(len(arr[0]) - 2):
            count += check_block(arr, r, c)
    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    arr = np.array([list(line.strip()) for line in lines], dtype=str)
    print(find_xmas(arr))
