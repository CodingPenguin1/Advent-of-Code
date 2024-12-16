class Warehouse:
    def __init__(self, warehouse_string: str):
        self.width = -1
        self.height = -1
        self.walls = []
        self.boxes = []
        self.robot = [0, 0]

        lines = warehouse_string.split("\n")
        self.height = len(lines)
        self.width = len(lines[0])
        for r, line in enumerate(lines):
            for c, char in enumerate(line):
                if char == "O":
                    self.boxes.append([r, c])
                elif char == "#":
                    self.walls.append([r, c])
                elif char == "@":
                    self.robot = [r, c]

    def __str__(self):
        s = ""
        for r in range(self.height):
            for c in range(self.width):
                if [r, c] == self.robot:
                    s += "@."
                elif [r, c] in self.walls:
                    s += "##"
                elif [r, c] in self.boxes:
                    s += "[]"
                else:
                    s += ".."
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
    with open("sample_input.txt") as f:
        text = f.read()

    warehouse_str, moves_str = text.split("\n\n")
    warehouse = Warehouse(warehouse_str)
    moves = moves_str.replace("\n", "")

    print(warehouse)

    # for move in moves:
    #     warehouse.move(move)
    # gps_coords = get_gps_coords(warehouse)
    # print(sum(gps_coords))
