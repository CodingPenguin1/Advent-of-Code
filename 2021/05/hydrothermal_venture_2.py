#!/usr/bin/env python

import numpy as np


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    arr = np.zeros((1000, 1000), dtype=int)
    for line in lines:
        point_a, point_b = line.split(' -> ')
        point_a = [int(i) for i in point_a.split(',')]
        point_b = [int(i) for i in point_b.split(',')]

        # If vertical line
        if point_a[0] == point_b[0]:
            x = point_a[0]
            ys = sorted([point_a[1], point_b[1]])
            for y in range(ys[0], ys[1] + 1):
                arr[y, x] += 1

        # If horizontal line
        elif point_a[1] == point_b[1]:
            y = point_a[1]
            xs = sorted([point_a[0], point_b[0]])
            for x in range(xs[0], xs[1] + 1):
                arr[y, x] += 1

        # If diagonal
        else:
            # Swap the points if point_b x coordinate is less than point_a x coordinate
            if point_b[0] < point_a[0]:
                point_a, point_b = point_b, point_a

            # If point_b y is greater than point_a y, just iterate
            if point_b[1] > point_a[1]:
                current_point = point_a
                arr[current_point[1], current_point[0]] += 1
                while current_point != point_b:
                    current_point[0] += 1
                    current_point[1] += 1
                    arr[current_point[1], current_point[0]] += 1

            # If point_b y is less than point_a y, iterate backwards
            if point_b[1] < point_a[1]:
                current_point = point_a
                arr[current_point[1], current_point[0]] += 1
                while current_point != point_b:
                    current_point[0] += 1
                    current_point[1] -= 1
                    arr[current_point[1], current_point[0]] += 1

    values, counts = np.unique(arr, return_counts=True)
    values, counts = list(values), list(counts)

    # Drop 0 and 1
    index_0 = values.index(0)
    values.remove(0)
    counts.pop(index_0)
    index_1 = values.index(1)
    values.remove(1)
    counts.pop(index_1)

    print(sum(counts))
