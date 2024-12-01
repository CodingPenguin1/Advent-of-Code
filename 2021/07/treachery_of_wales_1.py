#!/usr/bin/env python

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    crab_positions = [int(x) for x in lines[0].split(',')]
    potential_positions = [x for x in range(max(crab_positions) + 1)]
    fuel_burned = [0] * (max(potential_positions) + 1)

    for target in range(len(potential_positions)):
        for crab in crab_positions:
            fuel_burned[target] += abs(crab - potential_positions[target])

    print(min(fuel_burned))
