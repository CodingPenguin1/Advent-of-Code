with open("input.txt") as f:
    input_lines = f.readlines()

# Load input
l1, l2 = [], []
for line in input_lines:
    val_1, val_2 = [int(x) for x in line.split("   ")]
    l1.append(val_1)
    l2.append(val_2)

# Compute similarity scores
score = 0
for num in l1:
    score += num * l2.count(num)
print(score)
