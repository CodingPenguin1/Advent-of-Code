import re


def get_muls(s: str):
    muls = []
    for mul in re.findall(r"mul\(\d+,\d+\)", s):
        x = int(mul.split(",")[0][4:])
        y = int(mul.split(",")[1].strip(")"))
        muls.append(x * y)
    return muls


with open("input.txt") as f:
    lines = f.readlines()

_sum = 0
for line in lines:
    _sum += sum(get_muls(line))
print(_sum)
