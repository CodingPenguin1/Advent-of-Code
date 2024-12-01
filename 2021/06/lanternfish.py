#!/usr/bin/env python

import numpy as np

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    fish = [int(i) for i in lines[0].split(',')]

    fish_counts = np.zeros(9, dtype=int)
    for item in fish:
        fish_counts[item] += 1

    duration = 256
    for _ in range(duration):
        next_fish_counts = np.zeros(9, dtype=int)
        for i in range(len(fish_counts)):
            if i == 0:
                next_fish_counts[8] += fish_counts[0]
                next_fish_counts[6] += fish_counts[0]
            else:
                next_fish_counts[i - 1] += fish_counts[i]
        fish_counts = next_fish_counts

    print(sum(fish_counts))
