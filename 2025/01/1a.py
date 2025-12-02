def count_zeros(sequence: list[str], value: int = 50, val_range: tuple[int, int] = (0, 99)) -> int:
    zero = 0
    for turn in sequence:
        if turn[0] == "R":
            value += int(turn[1:])
            while value > val_range[1]:
                value -= val_range[1] + 1
        elif turn[0] == "L":
            value -= int(turn[1:])
            while value < val_range[0]:
                value += val_range[1] + 1

        if value == 0:
            zero += 1
        # print(turn, value)
    return zero


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    zero = count_zeros(lines)
    print(zero)
