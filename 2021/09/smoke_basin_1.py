#!/usr/bin/env python

import numpy as np


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    arr = np.zeros((len(lines), len(lines[0]) - 1), dtype=int)
    for i, line in enumerate(lines):
        for j, val in enumerate(line.strip()):
            arr[i, j] = int(val)

    risk = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            low_point = True
            # Check if left is smaller
            if j > 0 and arr[i, j] >= arr[i, j - 1]:
                low_point = False
            # Check if right is smaller
            if j < len(arr[0]) - 1 and arr[i, j] >= arr[i, j + 1]:
                low_point = False
            # Check if top is smaller
            if i > 0 and arr[i, j] >= arr[i - 1, j]:
                low_point = False
            # Check if bottom is smaller
            if i < len(arr) - 1 and arr[i, j] >= arr[i + 1, j]:
                low_point = False

            if low_point:
                risk += arr[i, j] + 1

    print(risk)
