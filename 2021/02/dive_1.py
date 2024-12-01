#!/usr/bin/env python


if __name__ == '__main__':
    depth = 0
    horiz = 0

    with open('input.txt') as f:
        for line in f:
            if line.startswith('forward'):
                horiz += int(line.split()[1])
            elif line.startswith('down'):
                depth += int(line.split()[1])
            elif line.startswith('up'):
                depth -= int(line.split()[1])

    print(depth * horiz)
