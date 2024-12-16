import numpy as np


class Warehouse:
    def __init__(self, warehouse_string: str):
        lines = warehouse_string.split("\n")
        self.grid = np.zeros((len(lines), len(lines[0])), dtype=np.int8)  # 0 empty, 1 box, -1 wall
        self.r, self.c = 0, 0

        for r, line in enumerate(lines):
            for c, char in enumerate(line):
                if char == "O":
                    self.grid[r][c] = 1
                elif char == "#":
                    self.grid[r][c] = -1
                elif char == "@":
                    self.r = r
                    self.c = c

    def _cycle(self, cells: np.ndarray[np.int8], left: bool = False) -> list[np.int8]:
        if len(cells) <= 1:
            return cells
        if 0 not in cells:
            return cells

        cells = list(cells)
        if left and cells[0] == 0:
            cells.append(cells.pop(0))

        elif cells[-1] == 0:
            cells.insert(0, cells.pop())

        return cells

    def move(self, move: str):
        if move == "^":
            end_r = -1  # Row of first non-box above the robot
            for r in range(self.r - 1, -1, -1):
                if self.grid[r][self.c] < 1:
                    end_r = r
                    break

            # Everything between the robot and the non-box space
            spaces = self.grid[end_r : self.r, self.c]
            spaces = self._cycle(spaces, left=True)
            if len(spaces) > 1:
                for r, cell in enumerate(spaces):
                    self.grid[end_r + r][self.c] = cell
            if self.grid[self.r - 1][self.c] == 0:
                self.r -= 1

        if move == "v":
            end_r = -1  # Row of first non-box below the robot
            for r in range(self.r + 1, self.grid.shape[0]):
                if self.grid[r][self.c] < 1:
                    end_r = r
                    break

            # Everything between the robot and the non-box space
            spaces = self.grid[self.r + 1 : end_r + 1, self.c]
            spaces = self._cycle(spaces)
            if len(spaces) > 1:
                for r, cell in enumerate(spaces):
                    self.grid[self.r + 1 + r][self.c] = cell
            if self.grid[self.r + 1][self.c] == 0:
                self.r += 1

        if move == ">":
            end_c = -1  # Column of first non-box to the right of the robot
            for c in range(self.c + 1, self.grid.shape[1]):
                if self.grid[self.r][c] < 1:
                    end_c = c
                    break

            # Everything between the robot and the non-box space
            spaces = self.grid[self.r, self.c + 1 : end_c + 1]
            spaces = self._cycle(spaces)
            if len(spaces) > 1:
                for c, cell in enumerate(spaces):
                    self.grid[self.r][self.c + 1 + c] = cell
            if self.grid[self.r][self.c + 1] == 0:
                self.c += 1

        if move == "<":
            end_c = -1  # Column of first non-box to the left of the robot
            for c in range(self.c - 1, -1, -1):
                if self.grid[self.r][c] < 1:
                    end_c = c
                    break

            # Everything between the robot and the non-box space
            spaces = self.grid[self.r, end_c : self.c]
            spaces = self._cycle(spaces, left=True)
            if len(spaces) > 1:
                for c, cell in enumerate(spaces):
                    self.grid[self.r][end_c + c] = cell
            if self.grid[self.r][self.c - 1] == 0:
                self.c -= 1

    def __str__(self):
        s = ""
        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                if (r, c) == (self.r, self.c):
                    s += "@"
                elif cell == -1:
                    s += "#"
                elif cell == 1:
                    s += "O"
                else:
                    s += "."
            s += "\n"
        return s


def get_gps_coords(warehouse: Warehouse):
    gps_coords = []
    for r, row in enumerate(warehouse.grid):
        for c, cell in enumerate(row):
            if cell == 1:
                gps_coords.append(100 * r + c)
    return gps_coords


if __name__ == "__main__":
    with open("input.txt") as f:
        text = f.read()

    warehouse_str, moves_str = text.split("\n\n")
    warehouse = Warehouse(warehouse_str)
    moves = moves_str.replace("\n", "")

    for move in moves:
        warehouse.move(move)
    gps_coords = get_gps_coords(warehouse)
    print(sum(gps_coords))
