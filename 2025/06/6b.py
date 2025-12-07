import numpy as np


def parse_values(raw: list[str]) -> list[list[int]]:
    all_values = []
    values = []
    for col in range(len(raw[0])):
        value = ""
        for row in range(len(raw)):
            value += raw[row][col]
        if value.strip() == "":
            all_values.append(list(reversed(values)))
            values = []
            continue
        values.append(int(value))
    all_values.append(list(reversed(values)))
    all_values.remove([])
    return list(reversed(all_values))


if __name__ == "__main__":
    with open("2025/06/input.txt") as f:
        lines = f.readlines()

    raw = []
    for line in lines:
        cleaned_line = line.split(" ")
        while " " in cleaned_line:
            cleaned_line.remove(" ")
        while "" in cleaned_line:
            cleaned_line.remove("")
        for i, val in enumerate(cleaned_line):
            if val.isdigit():
                cleaned_line[i] = int(val)
        raw.append(cleaned_line)

    all_values = parse_values(lines[:-1])
    operations = list(reversed(raw[-1]))
    if '\n' in operations:
        operations.remove("\n")

    sum_ = 0
    for values, operation in zip(all_values, operations, strict=True):
        if operation == "+":
            result = sum(values)
        else:
            result = np.array(values).prod()
        sum_ += result
    print(sum_)
