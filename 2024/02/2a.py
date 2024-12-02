def check_report(report: list[int]):
    ordered = False  # The levels are either all increasing or all decreasing
    similar_levels = False  # Any two adjacent levels differ by at least one and at most three

    # Check ordered
    ordered = sorted(report) == report or sorted(report, reverse=True) == report
    if not ordered:
        return False

    # Check similar levels
    adjacent_levels = [abs(report[i] - report[i + 1]) for i in range(len(report) - 1)]
    if all(0 < x < 4 for x in adjacent_levels):
        similar_levels = True
    return ordered and similar_levels


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    reports = [[int(x) for x in line.strip().split(" ")] for line in lines]

    safe_count = 0
    for report in reports:
        if check_report(report):
            safe_count += 1
    print(safe_count)
