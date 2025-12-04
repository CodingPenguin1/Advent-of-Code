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


def remove_rolls(rolls: np.array, to_remove: np.array) -> np.array:
    for r in range(len(rolls)):
        for c in range(len(rolls[0])):
            if to_remove[r][c] == 1:
                rolls[r][c] = "."
    return rolls


def get_valid_spot_arr(rolls: np.array) -> np.array:
    valid_spots = np.zeros(shape=rolls.shape)
    for r, row in enumerate(rolls):
        for c, cell in enumerate(row):
            if cell == "@":
                if check_cell(rolls, r, c):
                    valid_spots[r][c] = 1
    return valid_spots


if __name__ == "__main__":
    with open("2025/04/input.txt") as f:
        rolls = np.array([list(line.strip()) for line in f.readlines()])

    valid_spots = get_valid_spot_arr(rolls)
    removed_rolls = 0
    while valid_spots.sum():
        removed_rolls += valid_spots.sum()
        rolls = remove_rolls(rolls, valid_spots)
        valid_spots = get_valid_spot_arr(rolls)
    print(int(removed_rolls))
