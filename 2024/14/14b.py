import numpy as np

GRID_WIDTH = 101
GRID_HEIGHT = 103


class Robot:
    def __init__(self, r, c, r_v, c_v):
        self.r = r
        self.c = c
        self.r_v = r_v
        self.c_v = c_v

    def move(self):
        self.r += self.r_v
        self.c += self.c_v

        if self.r < 0:
            self.r = GRID_HEIGHT + self.r
        elif self.r >= GRID_HEIGHT:
            self.r %= GRID_HEIGHT

        if self.c < 0:
            self.c = GRID_WIDTH + self.c
        elif self.c >= GRID_WIDTH:
            self.c %= GRID_WIDTH

    def __str__(self):
        return f"p={self.c},{self.r} v={self.c_v},{self.r_v}"


def print_grid(robots: list[Robot]):
    for r in range(GRID_HEIGHT // 3, (2 * GRID_HEIGHT) // 3):
        for c in range(GRID_WIDTH // 4, (3 * GRID_WIDTH) // 4):
            robot_count = 0
            for robot in robots:
                if robot.r == r and robot.c == c:
                    robot_count += 1

            if robot_count:
                print("X", end="")
            else:
                print(".", end="")
        print()


def check_christmas_tree(robots: list[Robot]) -> bool:
    grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=np.uint8)
    for robot in robots:
        grid[robot.r][robot.c] = 1

    for robot in robots:
        found_10_vertical = True
        for c in range(robot.c, robot.c + 10):
            if c >= GRID_WIDTH or grid[robot.r][c] == 0:
                found_10_vertical = False
                break
        if found_10_vertical:
            return True
    return False


if __name__ == "__main__":
    input_file = "input.txt"
    if input_file.startswith("sample"):
        GRID_WIDTH = 11
        GRID_HEIGHT = 7

    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]

    robots = []
    for line in lines:
        line = line.replace("p", "").replace("v", "").replace("=", "")
        position, velocity = line.split(" ")
        c, r = [int(x) for x in position.split(",")]
        c_v, r_v = [int(x) for x in velocity.split(",")]
        robots.append(Robot(r, c, r_v, c_v))

    for i in range(1_000_000):
        for robot in robots:
            robot.move()
        if check_christmas_tree(robots):
            print_grid(robots)
            print(i + 1)
            exit()
