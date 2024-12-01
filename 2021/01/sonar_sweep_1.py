#!/usr/bin/env python


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [int(i) for i in lines]

        count = 0
        for i in range(1, len(lines)):
            if lines[i] > lines[i - 1]:
                count += 1

        print(count)
