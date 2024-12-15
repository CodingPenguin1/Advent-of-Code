import numpy as np


def solve_equations(x1, y1, x2, y2, x_ans, y_ans):
    terms = np.array([[x1, x2], [y1, y2]])
    answers = np.array([x_ans, y_ans])

    results = np.linalg.solve(terms, answers)
    a_presses, b_presses = tuple(round(x) for x in results)

    if a_presses < 0 or b_presses < 0:
        return 0, 0

    if check_answer(x1, x2, x_ans, a_presses, b_presses) and check_answer(y1, y2, y_ans, a_presses, b_presses):
        return a_presses, b_presses
    return 0, 0


def check_answer(a, b, c, x, y):
    return int(a) * int(x) + int(b) * int(y) == int(c)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
        lines.append("\n")

    equations = []
    cur_eq = []
    for line in lines:
        if line.startswith("Button"):
            sections = line.strip().split("+")
            x = int(sections[1][: sections[1].index(",")])
            y = int(sections[-1])
            cur_eq.extend([x, y])
        elif line.startswith("Prize"):
            sections = line.strip().split("=")
            x = int(sections[1][: sections[1].index(",")])
            y = int(sections[-1])
            cur_eq.extend([x, y])
        else:
            equations.append(cur_eq)
            cur_eq = []

    tokens = 0
    for equation in equations:
        presses = solve_equations(*equation)
        tokens += 3 * presses[0] + presses[1]
    print(tokens)
