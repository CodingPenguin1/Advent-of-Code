if __name__ == "__main__":
    ranges: list[tuple[int, int]] = []
    with open("2025/05/input.txt") as f:
        for line in f.readlines():
            if len(line.strip()) == 0:
                break
            ranges.append(tuple(map(int, line.strip().split("-"))))
    ranges.sort(key=lambda r: r[0])

    merged: list[tuple[int, int]] = []
    low, high = ranges[0]
    for new_low, new_high in ranges[1:]:
        if new_low <= high:
            high = max(high, new_high)
        else:
            merged.append((low, high))
            low, high = new_low, new_high
    merged.append((low, high))
    print(sum(r[1] - r[0] + 1 for r in merged))
