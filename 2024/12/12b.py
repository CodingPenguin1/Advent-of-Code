import numpy as np
from rich.progress import Progress


def flood_fill(arr, r, c, target_value, mask_arr):
    # Fill mask_arr with 1 if in area, 0 if not
    if arr[r][c] == target_value:
        mask_arr[r][c] = 1

    # Don't go back somewhere we've already gone
    if r + 1 < len(arr) and arr[r + 1][c] == target_value and mask_arr[r + 1][c] == 0:
        flood_fill(arr, r + 1, c, target_value, mask_arr)
    if r - 1 >= 0 and arr[r - 1][c] == target_value and mask_arr[r - 1][c] == 0:
        flood_fill(arr, r - 1, c, target_value, mask_arr)
    if c + 1 < len(arr) and arr[r][c + 1] == target_value and mask_arr[r][c + 1] == 0:
        flood_fill(arr, r, c + 1, target_value, mask_arr)
    if c - 1 >= 0 and arr[r][c - 1] == target_value and mask_arr[r][c - 1] == 0:
        flood_fill(arr, r, c - 1, target_value, mask_arr)

    return mask_arr


def get_area(arr: np.array):
    # Bool array
    area = 0
    for row in arr:
        for cell in row:
            if cell:
                area += 1
    return area


def get_perimeter(mask_arr: np.array):
    # Bool array
    # Double size of array in both dimensions to avoid 1-wide or 1-tall blocks
    arr = np.zeros((mask_arr.shape[0] * 2, mask_arr.shape[1] * 2), dtype=bool)
    for r, row in enumerate(mask_arr):
        for c, cell in enumerate(row):
            arr[2 * r][2 * c] = cell
            arr[2 * r + 1][2 * c] = cell
            arr[2 * r + 1][2 * c + 1] = cell
            arr[2 * r][2 * c + 1] = cell

    perimeter = 0
    for r, row in enumerate(arr):
        for c, cell in enumerate(row):
            if not cell:
                continue

            # Check if cell is outside corner
            if sum([arr[r + 1][c], arr[r - 1][c], arr[r][c + 1], arr[r][c - 1]]) == 2:
                perimeter += 1
            # Check if cell is inside
            elif np.sum(arr[r - 1 : r + 2, c - 1 : c + 2]) == 8:
                perimeter += 1

    return perimeter


def process_space(arr, r, c):
    # Flood fill starting at r, c
    mask_arr = np.zeros(arr.shape, dtype=bool)
    flood_fill(arr, r, c, arr[r][c], mask_arr)
    padded_arr = np.pad(mask_arr, pad_width=1, mode="constant", constant_values=0)

    area = get_area(padded_arr)
    perimeter = get_perimeter(padded_arr)

    masked_arr = np.copy(arr)
    for r, row in enumerate(mask_arr):
        for c, cell in enumerate(row):
            if cell:
                masked_arr[r][c] = 0

    return (area, perimeter, masked_arr)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    arr = np.zeros((len(lines), len(lines[0])), dtype=np.uint8)
    for r, line in enumerate(lines):
        for c, cell in enumerate(line):
            arr[r][c] = ord(cell) - 64

    areas, perimeters = [], []
    with Progress() as progress:
        task = progress.add_task("Processing", total=arr.shape[0] * arr.shape[1])
        for r in range(len(arr)):
            for c in range(len(arr[0])):
                progress.update(task, advance=1)
                if arr[r][c] == 0:
                    continue

                char = chr(arr[r][c] + 64)
                sub_area, sub_perimeter, arr = process_space(arr, r, c)
                areas.append(sub_area)
                perimeters.append(sub_perimeter)

    price = 0
    for area, perimeter in zip(areas, perimeters):
        price += area * perimeter
    print(price)
