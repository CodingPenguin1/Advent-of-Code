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


def test_remove_levels(report: list[int]):
    # If report is safe as is, don't try to remove levels
    if check_report(report):
        return True

    # Otherwise, try to remove each level until one works
    for i in range(len(report)):
        short_report = report[:i] + report[i + 1 :]
        if check_report(short_report):
            return True
    return False


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    reports = [[int(x) for x in line.strip().split(" ")] for line in lines]

    safe_count = 0
    for report in reports:
        if test_remove_levels(report):
            safe_count += 1
    print(safe_count)
