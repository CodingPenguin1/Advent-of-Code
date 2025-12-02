def count_zeros(sequence: list[str], value: int = 50) -> int:
    zero = 0
    for turn in sequence:
        direction = turn[0]
        count = int(turn[1:])
        print(value, end=" ")

        if direction == "R":
            zero += (value + count) // 100
            value = (value + count) % 100
        else:
            new_value = (value - count) % 100

            if value == 0:
                zero += count // 100
            elif count > value:
                zero += ((count - value - 1) // 100) + 1
                if new_value == 0:
                    zero += 1
            elif count == value:
                zero += 1
            value = new_value

        print(turn, value, zero)
    return zero


if __name__ == "__main__":
    with open("2025/01/input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    # lines = ["L150"]
    zero = count_zeros(lines)
    print(zero)
