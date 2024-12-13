def update(stone_counts: dict[str, int]) -> dict[str, int]:
    new_stone_counts = {}

    for stone, count in stone_counts.items():
        new_stones = []
        if stone == "0":
            new_stones = ["1"]
        elif len(stone) % 2 == 0:
            left, right = str(int(stone[: len(stone) // 2])), str(int(stone[len(stone) // 2 :]))
            new_stones = [left, right]
        else:
            new_stones = [str(int(stone) * 2024)]

        for stone in new_stones:
            if stone in new_stone_counts:
                new_stone_counts[stone] += count
            else:
                new_stone_counts[stone] = count
    return new_stone_counts


if __name__ == "__main__":
    with open("input.txt") as f:
        stones = f.readline().strip().split(" ")

    stone_counts = {}
    for stone in stones:
        if stone in stone_counts:
            stone_counts[stone] += 1
        else:
            stone_counts[stone] = 1

    for _ in range(75):
        stone_counts = update(stone_counts)
    print(sum(stone_counts.values()))
