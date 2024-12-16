class Warehouse:
    def __init__(self, warehouse_string: str):
        self.width = -1
        self.height = -1
        self.walls = []
        self.left_boxes = []
        self.right_boxes = []
        self.r, self.c = -1, -1

        lines = warehouse_string.split("\n")
        self.height = len(lines)
        self.width = len(lines[0]) * 2
        for r, line in enumerate(lines):
            for c, char in enumerate(line):
                if char == "O":
                    self.left_boxes.append([r, 2 * c])
                    self.right_boxes.append([r, 2 * c + 1])
                elif char == "#":
                    self.walls.append([r, 2 * c])
                    self.walls.append([r, 2 * c + 1])
                elif char == "@":
                    self.r, self.c = r, 2 * c

    def __str__(self):
        s = ""
        for r in range(self.height):
            for c in range(self.width):
                if [r, c] == [self.r, self.c]:
                    s += "@"
                elif [r, c] in self.walls:
                    s += "#"
                elif [r, c] in self.left_boxes:
                    s += "["
                elif [r, c] in self.right_boxes:
                    s += "]"
                else:
                    s += "."
            s += "\n"
        return s

    def _get_neighboring_boxes(self, boxes, direction):
        # For up or down only
        if direction not in {"^", "v"}:
            return boxes

        r_mod = -1 if direction == "^" else 1

        added_boxes = True
        while added_boxes:
            added_boxes = False
            for box in boxes:
                above = [box[0] + r_mod, box[1]]  # or below but I can't come up with a better var name rn
                if above in self.left_boxes and above not in boxes:
                    added_boxes = True
                    boxes.append(above)
                    boxes.append([above[0], above[1] + 1])
                if above in self.right_boxes and above not in boxes:
                    added_boxes = True
                    boxes.append(above)
                    boxes.append([above[0], above[1] - 1])

        return boxes

    def _is_moveable(self, boxes, direction):
        # For up or down only
        r_mod = -1 if direction == "^" else 1

        for box in boxes:
            if [box[0] + r_mod, box[1]] in self.walls:
                return False
        return True

    def move(self, direction: str):
        if direction == "<":
            # Find next non-box to the left
            for c in range(self.c - 1, -1, -1):
                if [self.r, c] in self.walls:
                    return
                if [self.r, c] not in self.left_boxes and [self.r, c] not in self.right_boxes:
                    for box in self.left_boxes:
                        if box[0] == self.r and c < box[1] < self.c:
                            box[1] -= 1
                    for box in self.right_boxes:
                        if box[0] == self.r and c < box[1] < self.c:
                            box[1] -= 1
                    self.c -= 1
                    return

        elif direction == ">":
            # Find next non-box to the right
            for c in range(self.c + 1, self.width):
                if [self.r, c] in self.walls:
                    return
                if [self.r, c] not in self.left_boxes and [self.r, c] not in self.right_boxes:
                    for box in self.left_boxes:
                        if box[0] == self.r and self.c < box[1] < c:
                            box[1] += 1
                    for box in self.right_boxes:
                        if box[0] == self.r and self.c < box[1] < c:
                            box[1] += 1
                    self.c += 1
                    return

        elif direction == "^":
            # Find next non-box to the right
            for r in range(self.r - 1, -1, -1):
                if [r, self.c] in self.walls:
                    return
                if [r, self.c] not in self.left_boxes and [r, self.c] not in self.right_boxes:
                    new_robot_space = [self.r - 1, self.c]
                    if new_robot_space in self.left_boxes or new_robot_space in self.right_boxes:
                        # Find what boxes to move
                        if [self.r - 1, self.c] in self.left_boxes:
                            move_boxes = [[self.r - 1, self.c], [self.r - 1, self.c + 1]]
                        else:
                            move_boxes = [[self.r - 1, self.c], [self.r - 1, self.c - 1]]
                        move_boxes = self._get_neighboring_boxes(move_boxes, "^")
                        # If boxes are moveable, move them
                        if self._is_moveable(move_boxes, "^"):
                            for box in self.left_boxes:
                                if box in move_boxes:
                                    box[0] -= 1
                            for box in self.right_boxes:
                                if box in move_boxes:
                                    box[0] -= 1

                    # Move robot
                    if new_robot_space not in self.walls and new_robot_space not in self.left_boxes and new_robot_space not in self.right_boxes:
                        self.r -= 1
                    return

        elif direction == "v":
            # Find next non-box to the right
            for r in range(self.r + 1, self.height):
                if [r, self.c] in self.walls:
                    return
                if [r, self.c] not in self.left_boxes and [r, self.c] not in self.right_boxes:
                    new_robot_space = [self.r + 1, self.c]
                    if new_robot_space in self.left_boxes or new_robot_space in self.right_boxes:
                        # Find what boxes to move
                        if [self.r + 1, self.c] in self.left_boxes:
                            move_boxes = [[self.r + 1, self.c], [self.r + 1, self.c + 1]]
                        else:
                            move_boxes = [[self.r + 1, self.c], [self.r + 1, self.c - 1]]
                        move_boxes = self._get_neighboring_boxes(move_boxes, "v")
                        # If boxes are moveable, move them
                        if self._is_moveable(move_boxes, "v"):
                            for box in self.left_boxes:
                                if box in move_boxes:
                                    box[0] += 1
                            for box in self.right_boxes:
                                if box in move_boxes:
                                    box[0] += 1

                    # Move robot
                    if new_robot_space not in self.walls and new_robot_space not in self.left_boxes and new_robot_space not in self.right_boxes:
                        self.r += 1
                    return


def get_gps_coords(warehouse: Warehouse) -> list[int]:
    gps_coords = []
    for box in warehouse.left_boxes:
        gps_coords.append(100 * box[0] + box[1])
    return gps_coords


if __name__ == "__main__":
    with open("input.txt") as f:
        text = f.read()

    warehouse_str, moves_str = text.split("\n\n")
    warehouse = Warehouse(warehouse_str)
    moves = moves_str.replace("\n", "")

    for move in moves:
        warehouse.move(move)
    print(sum(get_gps_coords(warehouse)))
