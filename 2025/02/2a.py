def is_invalid(val: int) -> bool:
    val = str(val)
    if val[: len(val) // 2] == val[len(val) // 2 :]:
        return True
    return False


def check_range(min_: int, max_: int) -> set[int]:
    invalid_ids: set[int] = set()
    for val in range(min_, max_ + 1):
        if is_invalid(val):
            invalid_ids.add(val)
    return invalid_ids


if __name__ == "__main__":
    with open("2025/02/input.txt") as f:
        line = f.readline().strip()
    sum_ = 0
    for range_ in line.split(","):
        min_, max_ = [int(x) for x in range_.split("-")]
        invalid_ids = check_range(min_, max_)
        sum_ += sum(invalid_ids)
    print(sum_)
