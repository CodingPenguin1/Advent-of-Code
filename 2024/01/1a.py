with open("input.txt") as f:
    input_lines = f.readlines()

# Load input
l1, l2 = [], []
for line in input_lines:
    val_1, val_2 = [int(x) for x in line.split("   ")]
    l1.append(val_1)
    l2.append(val_2)

# Sort lists
l1.sort()
l2.sort()

# Compute differences in list
differences = [(lambda i: abs(l1[i] - l2[i]))(i) for i in range(len(l1))]
print(sum(differences))
