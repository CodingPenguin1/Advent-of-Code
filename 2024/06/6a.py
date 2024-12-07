from lab import Lab

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    lab = Lab(lines)

    while not lab.guard_left:
        lab.move_guard()
    print(len(set(lab.guard_path)))
