def read_disk_map(disk_map: str) -> list:
    disk = []
    file_id = 0
    increment_file = False
    for i in range(len(disk_map)):
        if disk_map[i] == "0":
            increment_file = False
            continue
        for j in range(int(disk_map[i])):
            # If file, add file ID
            if not i % 2:
                disk.append(file_id)
                increment_file = True
            else:
                disk.append(".")
                increment_file = False
        if increment_file:
            file_id += 1
    return disk


def defrag(disk: list):
    free_index = 0
    for i in range(len(disk) - 1, 0, -1):
        for j in range(free_index, i):
            if j > i:
                break
            if disk[j] == ".":
                disk[j], disk[i] = disk[i], disk[j]
                free_index = j
                break

        if j > i:
            break
    return disk


def compute_checksum(disk: list):
    checksum = 0
    for i, block in enumerate(disk):
        if isinstance(block, int):
            checksum += i * block
    return checksum


if __name__ == "__main__":
    with open("input.txt") as f:
        disk_map = f.readline().strip()

    disk = read_disk_map(disk_map)
    disk = defrag(disk)
    checksum = compute_checksum(disk)
    print(checksum)
