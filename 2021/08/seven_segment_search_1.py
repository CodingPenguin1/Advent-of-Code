#!/usr/bin/env python

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        digits = line.strip().split(' | ')[1].split(' ')
        for digit in digits:
            if len(digit) in {2, 4, 3, 7}:
                count += 1
    print(count)
