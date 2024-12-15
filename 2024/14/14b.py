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
    for r in range(GRID_HEIGHT):
        if -1 < ((GRID_HEIGHT + 1) / 2) - r < 2:
            print()
        for c in range(GRID_WIDTH):
            robot_count = 0
            for robot in robots:
                if robot.r == r and robot.c == c:
                    robot_count += 1

            if abs(GRID_WIDTH // 2 - c) == 0:
                print(" ", end="")
            if robot_count:
                print(robot_count, end="")
            else:
                print(".", end="")
            if abs(GRID_WIDTH // 2 - c) == 0:
                print(" ", end="")
        print()


def get_safety_factor(robots: list[Robot]) -> int:
    v_mid = GRID_HEIGHT//2 if GRID_HEIGHT%2==0 else (GRID_HEIGHT)//2
    h_mid = GRID_WIDTH//2 if GRID_WIDTH%2==0 else (GRID_WIDTH)//2


    q1, q2, q3, q4 = 0, 0, 0, 0
    for r in range(GRID_HEIGHT):
        for c in range(GRID_WIDTH):
            if r == v_mid or c == h_mid:
                continue

            robot_count = 0
            for robot in robots:
                if robot.r == r and robot.c == c:
                    robot_count += 1

            if r < v_mid:
                if c < h_mid:
                    q1 += robot_count
                elif c > h_mid:
                    q2 += robot_count
            elif r > v_mid:
                if c < h_mid:
                    q3 += robot_count
                elif c > h_mid:
                    q4 += robot_count

    return q1 * q2 * q3 * q4


if __name__ == "__main__":
    input_file = 'input.txt'
    if input_file.startswith('sample'):
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

    # robots = [Robot(4, 2, -3, 2)]
    # print_grid(robots)
    # print("\n")
    # for _ in range(5):
    #     robots[0].move()
    #     print_grid(robots)
    #     print()

    SECONDS = 100
    for i in range(SECONDS):
        for robot in robots:
            robot.move()
        print_grid(robots)
        input(i)


    print_grid(robots)
    safety_factor = get_safety_factor(robots)
    print(safety_factor)
