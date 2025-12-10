import numpy as np


def get_start(arr: np.array) -> tuple[int, int]:
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if arr[r][c] == "S":
                return (r, c)


def process(arr: np.array):
    start = get_start(arr)
    data_arr = np.zeros(arr.shape, dtype=int)
    data_arr[start] = 1

    for r, row in enumerate(arr):
        if r == 0:
            continue
        for c, cell in enumerate(row):
            if cell == "^":
                first_time_left = bool(data_arr[r][c - 1])
                first_time_right = bool(data_arr[r][c + 1])
                data_arr[r][c - 1] += data_arr[r - 1][c - 1] + data_arr[r - 1][c]
                data_arr[r][c + 1] += data_arr[r - 1][c + 1] + data_arr[r - 1][c]
                if first_time_left and c - 2 >= 0 and arr[r][c - 2] == "^":
                    data_arr[r][c - 1] -= data_arr[r - 1][c - 1]
                if first_time_right and c + 2 < len(arr[0]) and arr[r][c + 2] == "^":
                    data_arr[r][c + 1] -= data_arr[r - 1][c + 1]
        for c, cell in enumerate(row):
            if cell == "." and data_arr[r][c] == 0 and data_arr[r - 1][c] > 0:
                data_arr[r][c] = data_arr[r - 1][c]

        # for row, data_row in zip(arr, data_arr):
        #     for cell, data_cell in zip(row, data_row):
        #         if data_cell > 0:
        #             print(hex(data_cell)[2:], end=" ")
        #         else:
        #             print(cell, end=" ")
        #     print()
        # print()
        # input()
    print(sum(data_arr[-1]))


if __name__ == "__main__":
    with open("2025/07/input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    arr = np.array([list(line) for line in lines])

    process(arr)
