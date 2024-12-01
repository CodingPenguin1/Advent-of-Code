#!/usr/bin/env python

import numpy as np


def flood_fill(arr, row, col, fill_num):
    if arr[row, col] == 0:
        arr[row, col] = fill_num
        if row > 0:
            arr = flood_fill(arr, row - 1, col, fill_num)
        if row < len(arr) - 1:
            arr = flood_fill(arr, row + 1, col, fill_num)
        if col > 0:
            arr = flood_fill(arr, row, col - 1, fill_num)
        if col < len(arr[0]) - 1:
            arr = flood_fill(arr, row, col + 1, fill_num)
    return arr


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    arr = np.zeros((len(lines), len(lines[0]) - 1), dtype=int)
    for i, line in enumerate(lines):
        for j, val in enumerate(line.strip()):
            arr[i, j] = int(val)

    # Fill walls of basins with -1
    basin_arr = np.zeros((len(lines), len(lines[0]) - 1), dtype=int)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i, j] == 9:
                basin_arr[i, j] = -1

    # Fill all basins with unique identifiers
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if basin_arr[i, j] == 0:
                basin_arr = flood_fill(basin_arr, i, j, basin_arr.max() + 1)

    values, counts = np.unique(basin_arr, return_index=False, return_inverse=False, return_counts=True, axis=None)
    values, counts = values[1:], counts[1:]  # Strip out 9s (basin walls)

    counts = list(counts)
    product = 1
    for _ in range(3):
        product *= max(counts)
        counts.remove(max(counts))
    print(product)
