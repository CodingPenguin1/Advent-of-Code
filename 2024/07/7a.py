from itertools import product
from simpleeval import simple_eval
from rich.progress import track


def solve_equation(expected_result: int, operands: list[int]) -> int:
    # https://stackoverflow.com/questions/3099987/how-can-i-get-permutations-with-repetitions-replacement-from-a-list-cartesian
    # Returns count of permutations that solved the equation
    operators = ["*", "+"]
    success_count = 0
    for combination in product(operators, repeat=len(operands) - 1):
        result = operands[0]
        for operator, operand in zip(combination, operands[1:]):
            result = simple_eval(f"{result} {operator} {operand}")

        if result == expected_result:
            success_count += 1
    return success_count


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    equations = []  # [(result, (operand_1, operand_2)), ...]
    for line in lines:
        result = int(line.split(":")[0])
        operands = tuple(int(x) for x in line.split(":")[1].strip().split(" "))
        equations.append((result, operands))

    _sum = 0
    for equation in track(equations, total=len(equations)):
        solution_count = solve_equation(*equation)
        if solution_count:
            _sum += equation[0]
    print(_sum)
