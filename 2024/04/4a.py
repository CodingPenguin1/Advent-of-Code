import numpy as np


def check_bounds(arr, r, c, r_end=0, c_end=0):
    return 0 <= r < len(arr) and 0 <= r_end <= len(arr) and 0 <= c < len(arr[0]) and 0 <= c_end <= len(arr[0])


def check_cell(arr: np.array, r: int, c: int):
    count = 0

    xmas_arr = list("XMAS")
    xmas_arr_reversed = list(reversed("XMAS"))

    # Check horizontal
    if check_bounds(arr, r, c, c_end=c + 4):
        section = list(arr[r, c : c + 4])
        count += section == xmas_arr or section == xmas_arr_reversed

    # Check vertical
    if check_bounds(arr, r, c, r_end=r + 4):
        section = list(arr[r : r + 4, c])
        count += section == xmas_arr or section == xmas_arr_reversed

    # Check diagonal
    if check_bounds(arr, r, c, r_end=r + 4, c_end=c + 4):
        # Top left to bottom right
        section = list(np.diag(arr[r : r + 4, c : c + 4]))
        count += section == xmas_arr or section == xmas_arr_reversed

        # Bottom left to top right
        section = list(np.diag(np.rot90(arr[r : r + 4, c : c + 4])))
        count += section == xmas_arr or section == xmas_arr_reversed

    return count


def find_xmas(arr: np.array):
    count = 0
    for r, row in enumerate(arr):
        for c, cell in enumerate(row):
            count += check_cell(arr, r, c)
    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    arr = np.array([list(line.strip()) for line in lines], dtype=str)
    print(find_xmas(arr))
