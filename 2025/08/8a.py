from itertools import combinations

import numpy as np


def cluster(arr: np.array, n_links: int = 10) -> list[int]:
    # Precompute all distances of all points
    distances: list[tuple[float, tuple[int, int]]] = []
    for pa_i, pb_i in combinations(range(len(arr)), 2):
        dist = np.linalg.norm(arr[pa_i] - arr[pb_i])
        distances.append((dist, (pa_i, pb_i)))
    distances.sort(key=lambda x: x[0])

    # Set up all points into their own clusters
    clusters = list(set([i]) for i in range(len(arr)))

    # Perform clustering on the first n_links pairs
    link_count = 0
    for dist, (pa_i, pb_i) in distances:
        print(f"merging {pa_i} and {pb_i}")
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
        print(clusters)
        print()

        link_count += 1
        if link_count == n_links:
            break

    return clusters


if __name__ == "__main__":
    with open("2025/08/input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    arr = np.array([line.split(",") for line in lines], dtype=int)
    clusters = cluster(arr, n_links=1000)
    counts = sorted([len(c) for c in clusters], reverse=True)
    print(counts)
    print(np.array(counts[:3]).prod())
