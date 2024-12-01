#!/usr/bin/env python
import numpy as np


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = [j for j in lines[i].strip()]

    arr = np.array(lines)
    arr = arr.transpose()
    gamma_bit_string = ''
    epsilon_bit_string = ''
    for i in range(len(arr)):
        values, counts = np.unique(arr[i], return_counts=True)
        if counts[1] > counts[0]:
            gamma_bit_string += str(values[1])
            epsilon_bit_string += str(values[0])
        else:
            gamma_bit_string += str(values[0])
            epsilon_bit_string += str(values[1])

    print(int(gamma_bit_string, 2) * int(epsilon_bit_string, 2))
