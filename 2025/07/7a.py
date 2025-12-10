import numpy as np


def splitter_is_hit(arr: np.array, splitter_row: int, splitter_col: int) -> bool:
    for row in range(splitter_row - 1, -1, -1):
        if arr[row][splitter_col] == "S":
            return True
        if arr[row][splitter_col] == "^":
            return False
        if arr[row][splitter_col - 1] == "^" or arr[row][splitter_col + 1] == "^":
            return True
    return False


if __name__ == "__main__":
    with open("2025/07/input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    arr = np.array([list(line) for line in lines])

    hit_splitters = []
    for r, row in enumerate(arr):
        for c, cell in enumerate(row):
            if cell == "^":
                if splitter_is_hit(arr, r, c):
                    hit_splitters.append((r, c))
    print(len(hit_splitters))
