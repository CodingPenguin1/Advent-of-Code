import numpy as np

import heapq
import sys


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


# def find_all_paths(grid, start, end):
#     rows, cols = grid.shape
#     visited = np.zeros((rows, cols), dtype=bool)
#     paths = []

#     # Directions for moving up, down, left, and right
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#     def dfs(x, y, path):
#         """Depth-first search to find all paths."""
#         if (x, y) == end:
#             paths.append(path.copy())
#             return

#         visited[x, y] = True

#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy
#             if is_valid_move(grid, nx, ny) and not visited[nx, ny]:
#                 path.append((nx, ny))
#                 dfs(nx, ny, path)
#                 path.pop()  # Backtrack

#         visited[x, y] = False

#     # Start DFS from the start position
#     dfs(start[0], start[1], [start])

#     return paths


# def find_all_paths(grid, start, end):
#     rows, cols = grid.shape
#     visited = np.zeros((rows, cols), dtype=bool)

#     # Directions for moving up, down, left, and right
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#     def dfs(x, y, path):
#         """Depth-first search to find all paths."""
#         if (x, y) == end:
#             yield path.copy()  # Yield the path as soon as it reaches the end

#         visited[x, y] = True

#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy
#             if is_valid_move(grid, nx, ny) and not visited[nx, ny]:
#                 path.append((nx, ny))
#                 yield from dfs(nx, ny, path)  # Yield paths found in recursive calls
#                 path.pop()  # Backtrack

#         visited[x, y] = False

#     # Start DFS from the start position
#     yield from dfs(start[0], start[1], [start])


def find_all_paths(grid, start, end):
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)

    # Directions for moving up, down, left, and right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def recursive_bfs(x, y, path):
        """Recursive BFS to find all paths."""
        print(abs(x - end[0]) + abs(y - end[1]))
        if (x, y) == end:
            yield path
            return

        visited[x, y] = True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid_move(grid, nx, ny) and not visited[nx, ny]:
                # Pass the current path to the next recursive call
                yield from recursive_bfs(nx, ny, path + [(nx, ny)])

        visited[x, y] = False

    # Start BFS from the start position
    yield from recursive_bfs(start[0], start[1], [start])


class TreeNode:
    """Tree node to represent a cell in the grid."""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.children = []


def build_path_tree(grid, start, end):
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def recursive_bfs(x, y, parent):
        """Recursive BFS to build the tree of all paths."""
        node = TreeNode(x, y)
        parent.children.append(node)

        if (x, y) == end:
            return node

        visited[x, y] = True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid_move(grid, nx, ny) and not visited[nx, ny]:
                recursive_bfs(nx, ny, node)

        visited[x, y] = False
        return node

    # Root of the tree starts at the start position
    root = TreeNode(start[0], start[1])
    recursive_bfs(start[0], start[1], root)

    return root


# Function to traverse the tree and collect all paths
def collect_paths(node, path=[]):
    """Traverse the tree and collect all paths."""
    path.append((node.x, node.y))
    if not node.children:
        yield path
    else:
        for child in node.children:
            yield from collect_paths(child, path.copy())
    path.pop()


def get_directions_from_path(path, initial_direction=3):
    dir_map = ["^", "v", "<", ">"]
    directions = [dir_map[initial_direction]]
    for i in range(1, len(path)):
        now = path[i]
        past = path[i - 1]
        if now[0] - 1 == past[0]:
            directions.append("v")
        elif now[0] + 1 == past[0]:
            directions.append("^")
        elif now[1] - 1 == past[1]:
            directions.append(">")
        elif now[1] + 1 == past[1]:
            directions.append("<")
    return directions


def get_turn_count(directions):
    count = 0
    for i in range(1, len(directions)):
        if directions[i] != directions[i - 1]:
            count += 1
    return count


if __name__ == "__main__":
    with open("input.txt") as f:
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

    path, best_cost = bfs(maze, start, end, initial_direction=2)

    sys.setrecursionlimit(10000)
    print(sys.getrecursionlimit())
    display_maze(maze, path)
    print(best_cost)

    path_tree_root = build_path_tree(maze, start, end)
    every_best_path_space = set()
    for path in collect_paths(path_tree_root):
        cost = 1000 * get_turn_count(get_directions_from_path(path)) + len(path) - 1
        if cost == best_cost:
            for space in path:
                every_best_path_space.add(space)
    display_maze(maze, every_best_path_space)
    print(len(every_best_path_space))

    # for path in find_all_paths(maze, start, end):
    #     print("hi")
    #     print(path)

    # all_paths = find_all_paths(maze, start, end)
    # every_best_path_space = set()
    # i = 0
    # for path in all_paths:
    #     i += 1
    #     print(i)
    #     # print(path)
    #     cost = 1000 * get_turn_count(get_directions_from_path(path)) + len(path) - 1
    #     if cost == best_cost:
    #         for space in path:
    #             every_best_path_space.add(space)

    # display_maze(maze, every_best_path_space)
    # print(len(every_best_path_space))
