from ast import literal_eval
from collections import deque

import numpy as np


def bfs(matrix, start_node, target_node):
    n = len(matrix)

    # Queue stores (current_node, path_list)
    queue = deque([(start_node, [start_node])])
    visited = {start_node}

    while queue:
        current_node, path = queue.popleft()

        # Target reached
        if current_node == target_node:
            # Extract weights for each step in the path
            # For a path [0, 1, 3], weights are matrix[0][1] and matrix[1][3]
            path_weights = [matrix[path[i]][path[i + 1]] for i in range(len(path) - 1)]
            return path, path_weights

        for neighbor in range(n):
            # If edge exists and neighbor hasn't been visited
            if matrix[current_node][neighbor] > -1 and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None, []


def push_button(state: int, button: tuple[int, ...], light_count: int) -> int:
    state_binary = bin(state)[2:].zfill(light_count)

    new_state = [bool(int(x)) for x in state_binary]
    for light_idx in button:
        new_state[light_idx] = not new_state[light_idx]

    new_state_str = "".join(str(int(x)) for x in new_state)
    return int(new_state_str, 2)


def light_int_to_string(light_int: int, light_count: int) -> str:
    light_string = ""
    for light in bin(light_int)[2:].zfill(light_count):
        if light == "1":
            light_string += "#"
        else:
            light_string += "."
    return light_string


class Machine:
    def __init__(self, string: str):
        target_light_string = string.split(" ")[0].replace("[", "").replace("]", "")
        button_string = string.split(" ")[1:-1]
        # joltage_string = string.split(" ")[-1]

        self.light_count = len(target_light_string)
        self.max_light = 2**self.light_count
        self.target_lights = int(target_light_string.replace("#", "1").replace(".", "0"), 2)
        self.buttons = [literal_eval(button.replace(")", ",)")) for button in button_string]

        self.adj_mat = np.full(fill_value=-1, shape=(self.max_light, self.max_light), dtype=int)
        for start_lights in range(self.max_light):
            for button_index, button in enumerate(self.buttons):
                end_lights = push_button(start_lights, button, self.light_count)
                self.adj_mat[start_lights][end_lights] = button_index

    def solve(self):
        path, edges = bfs(self.adj_mat, start_node=0, target_node=self.target_lights)
        buttons_pressed = []
        for i in edges:
            buttons_pressed.append(self.buttons[i])
        return buttons_pressed

    def demo_solution(self, solution: list[tuple[int, ...]]):
        lights = 0
        print(light_int_to_string(lights, self.light_count))
        for button in solution:
            lights = push_button(lights, button, self.light_count)
            print(light_int_to_string(lights, self.light_count))

    def manual(self):
        lights = 0
        print(light_int_to_string(lights, self.light_count))
        while True:
            ipt = input()
            if ipt == "q":
                break
            button = self.buttons[int(ipt)]
            lights = push_button(lights, button, self.light_count)
            print(light_int_to_string(lights, self.light_count))

    def __str__(self):
        light_string = light_int_to_string(self.target_lights, self.light_count)
        button_string = " ".join(str(b) for b in self.buttons)
        return f"[{light_string}] {button_string} {{}}"


if __name__ == "__main__":
    sum_ = 0
    with open("2025/10/input.txt") as f:
        machines = []
        for line in f.readlines():
            machine = Machine(line.strip())
            print(f"Solving machine:\n{machine}\n")
            solution = machine.solve()
            print(solution)
            # machine.demo_solution(solution)
            # machine.manual()
            sum_ += len(solution)
            print()
    print(sum_)
