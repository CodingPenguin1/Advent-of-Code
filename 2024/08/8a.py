from itertools import combinations

from math import dist


class Map:
    def __init__(self, grid: list[str]):
        self.width = len(grid[0].strip())
        self.height = len(grid)
        self.antennas = {}  # {'antenna_char': [(row, col), ...]}
        self.antinodes = {}  # ^^^

        for r, row in enumerate(grid):
            for c, char in enumerate(row.strip()):
                # Empty space, ignore
                if char == ".":
                    continue

                # Antenna
                if char not in self.antennas:
                    self.antennas[char] = [(r, c)]
                    self.antinodes[char] = []
                else:
                    self.antennas[char].append((r, c))

    def _is_antinode(self, point: tuple[int, int], antenna_a: tuple[int, int], antenna_b: tuple[int, int]):
        antenna_dist = dist(antenna_a, antenna_b)
        a_dist = dist(point, antenna_a)
        b_dist = dist(point, antenna_b)
        if a_dist == antenna_dist and b_dist == 2 * antenna_dist:
            return True
        if b_dist == antenna_dist and a_dist == 2 * antenna_dist:
            return True
        return False

    def _is_in_bounds(self, point):
        return 0 <= point[0] < self.height and 0 <= point[1] < self.width

    def __str__(self):
        s = ""
        for r in range(self.height):
            for c in range(self.width):
                antinode, antenna = "", ""
                for char, coords in self.antinodes.items():
                    if (r, c) in coords:
                        antinode = "#"
                for char, coords in self.antennas.items():
                    if (r, c) in coords:
                        antenna = char
                if antinode:
                    s += antinode
                elif antenna:
                    s += antenna
                else:
                    s += "."
            s += "\n"
        s += "\n"
        return s


def generate_antinodes(map: Map):
    for char in map.antennas.keys():
        for antenna_pair in combinations(map.antennas[char], 2):
            antenna_a, antenna_b = antenna_pair
            dy = antenna_a[0] - antenna_b[0]
            dx = antenna_a[1] - antenna_b[1]

            for dy_mod in (-1, 1):
                for dx_mod in (-1, 1):
                    test_point_a = (antenna_a[0] - (dy_mod * dy), antenna_a[1] - (dx_mod * dx))
                    test_point_b = (antenna_b[0] + (dy_mod * dy), antenna_b[1] + (dx_mod * dx))
                    if map._is_antinode(test_point_a, antenna_a, antenna_b) and map._is_in_bounds(test_point_a):
                        map.antinodes[char].append(test_point_a)
                    if map._is_antinode(test_point_b, antenna_a, antenna_b) and map._is_in_bounds(test_point_b):
                        map.antinodes[char].append(test_point_b)
    return map.antinodes


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    map = Map(lines)

    all_antinodes = []
    for _, antinodes in generate_antinodes(map).items():
        all_antinodes.extend(antinodes)
    print(len(set(all_antinodes)))
