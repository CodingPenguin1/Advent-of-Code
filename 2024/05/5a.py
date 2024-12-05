def get_rules(lines: list[str]) -> list[tuple[int, int]]:
    rules = []
    for line in lines:
        if line == "\n":
            break
        rules.append(tuple(int(x) for x in line.strip().split("|")))
    return rules


def get_updates(lines: list[str]) -> list[int]:
    in_update_section = False
    updates = []
    for line in lines:
        if in_update_section:
            updates.append([int(x) for x in line.strip().split(",")])

        if line == "\n":
            in_update_section = True
    return updates


def check_update(update: list[int], rules: list[tuple[int, int]]) -> bool:
    for rule in rules:
        # If both rule page numbers aren't in the update, skip this rule
        if not (rule[0] in update and rule[1] in update):
            continue

        # If the page number of the left side of the rule appears before the page number on the right side of the rule, we're good
        if update.index(rule[0]) > update.index(rule[1]):
            return False
    return True


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    rules = get_rules(lines)
    updates = get_updates(lines)

    _sum = 0
    for update in updates:
        if check_update(update, rules):
            _sum += update[len(update) // 2]
    print(_sum)
