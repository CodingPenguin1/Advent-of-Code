import numpy as np


def traverse(grid: np.array, r: int, c: int, paths: list = None, current_path: str = "") -> int:
    if paths is None:
        paths = []

    cur_val = grid[r][c]
    # Recursive traversal
    if cur_val == 9:
        paths.append(current_path)
        return paths

    # Check all directions for adjacent path 1 higher than current value
    if r + 1 < len(grid) and grid[r + 1][c] == cur_val + 1:
        current_path += "D"
        traverse(grid, r + 1, c, paths, current_path)
    if r - 1 >= 0 and grid[r - 1][c] == cur_val + 1:
        current_path += "U"
        traverse(grid, r - 1, c, paths, current_path)
    if c + 1 < len(grid) and grid[r][c + 1] == cur_val + 1:
        current_path += "R"
        traverse(grid, r, c + 1, paths, current_path)
    if c - 1 >= 0 and grid[r][c - 1] == cur_val + 1:
        current_path += "L"
        traverse(grid, r, c - 1, paths, current_path)
    return paths


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    grid = np.zeros((len(lines), len(lines[0])), dtype=np.int8)
    for r, line in enumerate(lines):
        for c, cell in enumerate(line):
            try:
                grid[r][c] = int(cell)
            except ValueError:
                grid[r][c] = -1

    count = 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == 0:
                paths = traverse(grid, r, c)
                count += len(set(paths))
    print(count)
