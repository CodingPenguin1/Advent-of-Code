import numpy as np


def traverse(grid: np.array, r: int, c: int, endpoints: set[tuple[int, int]] = None) -> int:
    if endpoints is None:
        endpoints = set()

    cur_val = grid[r][c]
    # Recursive traversal
    if cur_val == 9:
        endpoints.add((r, c))
        return endpoints

    # Check all directions for adjacent path 1 higher than current value
    if r + 1 < len(grid) and grid[r + 1][c] == cur_val + 1:
        endpoints.update(traverse(grid, r + 1, c, endpoints))
    if r - 1 >= 0 and grid[r - 1][c] == cur_val + 1:
        endpoints.update(traverse(grid, r - 1, c, endpoints))
    if c + 1 < len(grid) and grid[r][c + 1] == cur_val + 1:
        endpoints.update(traverse(grid, r, c + 1, endpoints))
    if c - 1 >= 0 and grid[r][c - 1] == cur_val + 1:
        endpoints.update(traverse(grid, r, c - 1, endpoints))
    return endpoints


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
                count += len(paths)
    print(count)
