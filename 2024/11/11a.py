def update(stones: list[str]) -> list[str]:
    new_list = []
    for stone in stones:
        if stone == "0":
            new_list.append("1")
        elif len(stone) % 2 == 0:
            left, right = str(int(stone[: len(stone) // 2])), str(int(stone[len(stone) // 2 :]))
            new_list.extend([left, right])
        else:
            new_list.append(str(int(stone) * 2024))
    return new_list


if __name__ == "__main__":
    with open("input.txt") as f:
        stones = f.readline().strip().split(" ")
    for _ in range(25):
        stones = update(stones)
    print(len(stones))
