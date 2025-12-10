from itertools import combinations

import numpy as np


def cluster(arr: np.array) -> int:
    # Precompute all distances of all points
    distances: list[tuple[float, tuple[int, int]]] = []
    for pa_i, pb_i in combinations(range(len(arr)), 2):
        dist = np.linalg.norm(arr[pa_i] - arr[pb_i])
        distances.append((dist, (pa_i, pb_i)))
    distances.sort(key=lambda x: x[0])

    # Set up all points into their own clusters
    clusters = list(set([i]) for i in range(len(arr)))

    # Perform clustering until there's only one cluster
    for dist, (pa_i, pb_i) in distances:
        for i, cluster in enumerate(clusters):
            if pa_i in cluster:
                pa_c = cluster
                pa_c_i = i
            if pb_i in cluster:
                pb_c = cluster
                pb_c_i = i
        if pa_c != pb_c:
            clusters[pa_c_i] = pa_c.union(pb_c)
            clusters.pop(pb_c_i)

        if len(clusters) == 1:
            print(arr[pa_i][0] * arr[pb_i][0])
            break


if __name__ == "__main__":
    with open("2025/08/input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    arr = np.array([line.split(",") for line in lines], dtype=int)
    cluster(arr)
