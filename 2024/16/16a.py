import numpy as np

import heapq


def display_maze(maze: np.ndarray, path=None):
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell:
                print("\u2588", end="")
            else:
                if path is not None and (r, c) in path:
                    print("X", end="")
                else:
                    print(".", end="")
        print()


def is_valid_move(grid, x, y):
    """Check if the move is valid."""
    rows, cols = grid.shape
    return 0 <= x < rows and 0 <= y < cols and not grid[x, y]


def bfs(grid, start, end, initial_direction=3):
    rows, cols = grid.shape
    visited = np.zeros((rows, cols, 4), dtype=bool)  # Track visited states for each direction
    pq = []  # Priority queue for cost-based BFS

    # Assume starting facing right (direction index 3)
    heapq.heappush(pq, (0, start[0], start[1], initial_direction, [start]))  # (total_cost, x, y, direction, path)

    # Directions for moving up, down, left, and right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    TURN_PENALTY = 1000  # Penalty for turning

    while pq:
        total_cost, current_r, current_c, current_dir, path = heapq.heappop(pq)

        # If the end is reached, return the path
        if (current_r, current_c) == end:
            return path, total_cost

        # Explore neighbors
        for i, (dr, dc) in enumerate(directions):
            next_r, next_c = current_r + dr, current_c + dc

            if is_valid_move(grid, next_r, next_c):
                move_cost = 1
                turn_cost = TURN_PENALTY if current_dir != i else 0
                next_cost = total_cost + move_cost + turn_cost

                if not visited[next_r, next_c, i]:
                    visited[next_r, next_c, i] = True
                    heapq.heappush(pq, (next_cost, next_r, next_c, i, path + [(next_r, next_c)]))

    return [], -1  # No path found


if __name__ == "__main__":
    with open("sample_input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    maze = np.zeros((len(lines), len(lines[0])), dtype=bool)
    start = -1, -1
    end = -1, -1
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == "#":
                maze[r][c] = True
            if char == "S":
                start = r, c
            elif char == "E":
                end = r, c

    path, cost = bfs(maze, start, end, initial_direction=2)

    display_maze(maze, path)
    print(cost)
