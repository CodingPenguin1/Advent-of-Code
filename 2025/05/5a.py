def check_ingredient(id_: int, fresh_ranges: list[tuple[int, int]]) -> bool:
    for fresh_range in fresh_ranges:
        if fresh_range[0] <= id_ <= fresh_range[1]:
            return True
    return False


if __name__ == "__main__":
    with open("2025/05/input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    fresh_ranges: list[tuple[int, int]] = []
    ingredient_ids: list[int] = []
    for line in lines:
        if "-" in line:
            fresh_ranges.append(tuple(int(x) for x in line.split("-")))
        elif len(line):
            ingredient_ids.append(int(line))

    print(fresh_ranges)
    print(ingredient_ids)
    count = 0
    for ingredient in ingredient_ids:
        count += int(check_ingredient(ingredient, fresh_ranges))
    print(count)
