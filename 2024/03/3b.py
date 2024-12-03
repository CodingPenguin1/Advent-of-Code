import re


def get_muls(s: str, enabled: bool = True):
    muls = []
    for mul in re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", s):
        print(mul, enabled)
        if mul == "don't()":
            enabled = False
        elif mul == "do()":
            enabled = True
        else:
            if enabled:
                x = int(mul.split(",")[0][4:])
                y = int(mul.split(",")[1].strip(")"))
                muls.append(x * y)
    return muls, enabled


with open("input.txt") as f:
    lines = f.readlines()

_sum = 0
enabled = True
for line in lines:
    line_muls, enabled = get_muls(line, enabled)
    _sum += sum(line_muls)
print(_sum)
