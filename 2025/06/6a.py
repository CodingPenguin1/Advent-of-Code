import numpy as np

if __name__ == "__main__":
    with open("2025/06/input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

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

    all_values = np.array(raw[:-1], dtype=int).transpose()
    operations = raw[-1]
    print(all_values)
    print(operations)

    sum_ = 0
    for values, operation in zip(all_values, operations, strict=True):
        print(values, operation)
        match operation:
            case "+":
                sum_ += sum(values)
            case "*":
                sum_ += values.prod()
    print(sum_)
