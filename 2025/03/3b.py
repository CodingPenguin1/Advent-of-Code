def find_biggest_idx(bank: str, start_idx: int, block_idxs: list[str]) -> int:
    """Find the index of the biggest value, left to right, excluding block_idxs.

    This performs a left->right search across the bank, starting at start_idx,
    and skipping values in block_idxs. This means that it'll find the biggest value
    to the right of previously calculated batteries, but to the left of uncomputed batteries.

    Args:
        bank (str): Battery bank.
        start_idx (int): Index to start looking at, moving right from here.
        block_idxs (list[str]): Indexes to skip consideration for.

    Returns:
        int: Index with the largest value in the bank.
    """
    best_idx = start_idx
    best_val = int(bank[start_idx])
    for i in range(start_idx, len(bank)):
        if i in block_idxs:
            continue
        if (new_val := int(bank[i])) > best_val:
            best_val = new_val
            best_idx = i
    return best_idx


def get_joltage(bank: str) -> int:
    """Given a battery bank, find the max joltage.

    Start by assuming the rightmost indicies contain the best value.
    Then, remove the first index (len-12). Move it to index 0
    Iterate to the right until you hit the indicies of the assumed "best" batteries
    Max value you found along there is the best value for the first battery.
    Do the same for the second battery, but instead of starting at 0, start
    at the battery just to the right of the first battery.
    Repeat for all batteries.

    Args:
        bank (str): Bank.

    Returns:
        int: Max joltage of the bank.
    """
    indicies = list(range(len(bank) - 12, len(bank)))
    for i in range(len(indicies)):
        start_idx = 0  # Where in the bank to start looking
        if i > 0:
            start_idx = indicies[i - 1] + 1

        block_idxs = indicies[:i] + indicies[i + 1 :]

        indicies[i] = find_biggest_idx(bank, start_idx, block_idxs)
    joltage = int("".join(bank[i] for i in indicies))
    return joltage


if __name__ == "__main__":
    with open("2025/03/input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    sum_ = sum(get_joltage(line) for line in lines)
    print(sum_)
