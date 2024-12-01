#!/usr/bin/env python

from math import inf


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [int(i) for i in lines]

        count = 0
        prev_sum = inf
        for i in range(2, len(lines)):
            cur_sum = lines[i - 2] + lines[i - 1] + lines[i]
            if cur_sum > prev_sum:
                count += 1
            prev_sum = cur_sum

        print(count)
