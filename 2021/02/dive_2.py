#!/usr/bin/env python


if __name__ == '__main__':
    depth = 0
    horiz = 0
    aim = 0

    with open('input.txt') as f:
        for line in f:
            if line.startswith('forward'):
                horiz += int(line.split()[1])
                depth += aim * int(line.split()[1])
            elif line.startswith('down'):
                aim += int(line.split()[1])
            elif line.startswith('up'):
                aim -= int(line.split()[1])

    print(depth * horiz)
