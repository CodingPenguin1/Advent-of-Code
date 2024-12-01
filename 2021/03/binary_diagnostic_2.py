#!/usr/bin/env python


def get_bit_value_counts(lines, index):
    counts = {'0': 0, '1': 0}
    for i in range(len(lines)):
        counts[lines[i][index]] += 1
    return counts


def o2(lines):
    for index in range(len(lines[i])):
        counts = get_bit_value_counts(lines, index)
        keep_bit_value = '1' if counts['1'] >= counts['0'] else '0'
        lines = [line for line in lines if line[index] == keep_bit_value]
        if len(lines) == 1:
            return int(lines[0], 2)


def co2(lines):
    for index in range(len(lines[i])):
        counts = get_bit_value_counts(lines, index)
        keep_bit_value = '0' if counts['0'] <= counts['1'] else '1'
        lines = [line for line in lines if line[index] == keep_bit_value]
        if len(lines) == 1:
            return int(lines[0], 2)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip()

    o2 = o2(lines)
    co2 = co2(lines)
    print(o2 * co2)
