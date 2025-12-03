def get_big_num(s: str) -> str:
    return str(max([int(c) for c in s]))


if __name__ == "__main__":
    with open("2025/03/input.txt") as f:
        lines = [l.strip() for l in f.readlines()]

    sum_ = 0
    for line in lines:
        biggest_num = get_big_num(line[:-1])
        idx = line.index(biggest_num)
        second_num = get_big_num(line[idx + 1 :])
        sum_ += int(biggest_num + second_num)
    print(sum_)
