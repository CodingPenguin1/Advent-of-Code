#!/usr/bin/env python
import numpy as np
from numba import jit


@jit
def process(crab_positions, potential_positions, fuel_burned):
    for target in range(len(potential_positions)):
        for crab in crab_positions:
            for i in range(abs(crab - potential_positions[target]) + 1):
                fuel_burned[target] += i

    print(min(fuel_burned))


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    crab_positions = np.array([int(x) for x in lines[0].split(',')])
    potential_positions = np.array([x for x in range(max(crab_positions) + 1)])
    fuel_burned = np.array([0] * (max(potential_positions) + 1))

    process(crab_positions, potential_positions, fuel_burned)
