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
    i = len(disk) - 1
    while i >= 0:
        print(i)
        # Don't move free space
        if disk[i] == ".":
            i -= 1
            continue

        # Find file range
        file_end_idx = i + 1
        for file_start_idx in range(file_end_idx):
            if disk[file_start_idx] == disk[i]:
                break

        # Find suitable free space to the left of the file
        file_size = file_end_idx - file_start_idx
        free_space_end_idx = -1
        for free_space_start_idx in range(file_start_idx):
            if all([block == "." for block in disk[free_space_start_idx : free_space_start_idx + file_size]]):
                free_space_end_idx = free_space_start_idx + file_size
                break

        if free_space_end_idx != -1:
            disk[file_start_idx:file_end_idx], disk[free_space_start_idx:free_space_end_idx] = (
                disk[free_space_start_idx:free_space_end_idx],
                disk[file_start_idx:file_end_idx],
            )
            i = file_start_idx

        if disk[i] != ".":
            i = file_start_idx - 1

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
