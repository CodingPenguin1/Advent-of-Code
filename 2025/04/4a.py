import numpy as np


def check_cell(grid: np.array, row: int, col: int) -> bool:
    paper_count = 0
    for r in range(row - 1, row + 2):
        if r < 0 or r >= len(grid):
            continue
        for c in range(col - 1, col + 2):
            if c < 0 or c >= len(grid[0]):
                continue
            if r == row and c == col:
                continue
            if grid[r][c] == "@":
                paper_count += 1
    return paper_count < 4


if __name__ == "__main__":
    with open("2025/04/input.txt") as f:
        grid = np.array([list(line.strip()) for line in f.readlines()])

    valid_spots = np.zeros(shape=grid.shape)
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "@":
                if check_cell(grid, r, c):
                    valid_spots[r][c] = 1
    print(int(valid_spots.sum()))
