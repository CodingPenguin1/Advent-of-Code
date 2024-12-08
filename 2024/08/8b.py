from itertools import combinations


class Map:
    def __init__(self, grid: list[str]):
        self.width = len(grid[0].strip())
        self.height = len(grid)
        self.antennas = {}  # {'antenna_frequency': [(row, col), ...]}
        self.antinodes = {}  # ^^^

        for r, row in enumerate(grid):
            for c, frequency in enumerate(row.strip()):
                # Empty space, ignore
                if frequency == ".":
                    continue

                # Antenna
                if frequency not in self.antennas:
                    self.antennas[frequency] = [(r, c)]
                    self.antinodes[frequency] = []
                else:
                    self.antennas[frequency].append((r, c))

    def _is_in_bounds(self, point):
        return 0 <= point[0] < self.height and 0 <= point[1] < self.width

    def __str__(self):
        s = ""
        for r in range(self.height):
            for c in range(self.width):
                antinode, antenna = "", ""
                for frequency, coords in self.antinodes.items():
                    if (r, c) in coords:
                        antinode = "#"
                for frequency, coords in self.antennas.items():
                    if (r, c) in coords:
                        antenna = frequency
                if antinode:
                    s += antinode
                elif antenna:
                    s += antenna
                else:
                    s += "."
            s += "\n"
        s += "\n"
        return s


def get_antinode_frequencies(map, point: tuple[int, int]) -> bool:
    frequencies = []
    for frequency in map.antennas.keys():
        for antenna_a, antenna_b in combinations(map.antennas[frequency], 2):
            # Handle vertical line
            if antenna_a[0] == antenna_b[0]:
                if point[0] == antenna_b[0]:
                    frequencies.append(frequency)
                    continue

            # Handle point is on antenna
            if point in map.antennas[frequency]:
                if len(map.antennas[frequency]) > 1:
                    frequencies.append(frequency)
                continue

            # Line is not vertical, slopes must be the same
            m = (antenna_b[0] - antenna_a[0]) / (antenna_b[1] - antenna_a[1])
            try:
                m2 = (point[0] - antenna_a[0]) / (point[1] - antenna_a[1])
                if m == m2 and map._is_in_bounds(point):
                    frequencies.append(frequency)
            except ZeroDivisionError:
                continue
    return frequencies


def generate_antinodes(map: Map):
    for r in range(map.height):
        for c in range(map.width):
            for frequency in get_antinode_frequencies(map, (r, c)):
                map.antinodes[frequency].append((r, c))
    return map.antinodes


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    map = Map(lines)

    all_antinodes = []
    for _, antinodes in generate_antinodes(map).items():
        all_antinodes.extend(antinodes)
    print(len(set(all_antinodes)))
