import numpy as np


class Lab:
    def __init__(self, grid: list[str]):
        self.grid = np.array([])
        self.guard = (0, 0)
        self.guard_facing = 0  # 0-up, 1-right, 2-down, 3-left
        self.guard_path = []  # [(row, col), ...]
        self.guard_direction_history = []
        self.turn_points = []
        self.guard_left = False  # True once the guard leaves the lab
        self._init_grid(grid)

    def _init_grid(self, grid):
        grid = np.array([[c for c in line.strip()] for line in grid])

        # 0 is space, 1, is wall
        self.grid = np.zeros(shape=grid.shape, dtype=bool)
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == "#":
                    self.grid[r][c] = 1
                elif cell == "^":
                    self.guard = (r, c)
                    self.guard_path.append(self.guard)
                    self.guard_direction_history.append(self.guard_facing)

    def _check_bounds_in_front(self):
        # Return true if space in front is in bounds, false if out of lab
        match self.guard_facing:
            case 0:
                return self.guard[0] - 1 >= 0
            case 1:
                return self.guard[1] + 1 < len(self.grid[0])
            case 2:
                return self.guard[0] + 1 < len(self.grid)
            case 3:
                return self.guard[1] - 1 >= 0

    def _check_space_in_front(self):
        # Return true if there's a wall, false if no wall
        r, c = self.guard
        match self.guard_facing:
            case 0:
                return self.grid[r - 1][c]
            case 1:
                return self.grid[r][c + 1]
            case 2:
                return self.grid[r + 1][c]
            case 3:
                return self.grid[r][c - 1]

    def _walk_forward(self):
        # Assumes space in front is clear
        match self.guard_facing:
            case 0:
                self.guard = (self.guard[0] - 1, self.guard[1])
            case 1:
                self.guard = (self.guard[0], self.guard[1] + 1)
            case 2:
                self.guard = (self.guard[0] + 1, self.guard[1])
            case 3:
                self.guard = (self.guard[0], self.guard[1] - 1)
        self.guard_path.append(self.guard)
        self.guard_direction_history.append(self.guard_facing)

    def move_guard(self):
        # If guard is already out of the lab, do nothing
        if self.guard_left:
            return

        # Check if we're about to walk out of the lab (off the grid)
        if not self._check_bounds_in_front():
            self.guard_left = True
            return

        # Check if the guard needs to turn before moving
        turn = self._check_space_in_front()

        # Move the guard
        if turn:
            self.turn_points.append((self.guard, self.guard_facing))
            self.guard_facing = (self.guard_facing + 1) % 4
        else:
            self._walk_forward()
        return turn

    def __str__(self):
        s = ""
        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                if (r, c) == self.guard:
                    s += ["^", ">", "v", "<"][self.guard_facing]
                elif (r, c) in self.guard_path:
                    s += "X"
                else:
                    if cell:
                        s += "#"
                    else:
                        s += "."
            s += "\n"
        return s
