from itertools import combinations

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


def get_area(p1: Point, p2: Point) -> int:
    x = abs(p1.x - p2.x) + 1
    y = abs(p1.y - p2.y) + 1
    return int(x * y)


if __name__ == "__main__":
    with open("2025/09/input.txt") as f:
        lines = f.readlines()

    tile_coords = [Point(int(x) for x in line.strip().split(",")) for line in lines]
    polygon = Polygon(tile_coords)

    max_area = 0
    for p1, p2 in combinations(tile_coords, 2):
        rectangle = Polygon([p1, Point(p2.x, p1.y), p2, Point(p1.x, p2.y)])
        if polygon.contains(rectangle):
            max_area = max(max_area, get_area(p1, p2))
    print(max_area)
