from itertools import combinations


def get_area(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    x = abs(p1[0] - p2[0]) + 1
    y = abs(p1[1] - p2[1]) + 1
    return x * y


if __name__ == "__main__":
    with open("2025/09/input.txt") as f:
        lines = f.readlines()

    tile_coords = [tuple(int(x) for x in line.strip().split(",")) for line in lines]
    max_area = 0
    for p1, p2 in combinations(tile_coords, 2):
        area = get_area(p1, p2)
        max_area = max(max_area, area)
    print(max_area)
