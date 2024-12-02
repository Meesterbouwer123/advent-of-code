def issafe(list: list[str], skip_index = -1):
    start = 1 if skip_index == 0 else 0
    last = int(list[start])
    sign = 0
    for i in range(start + 1, len(list)):
        if i == skip_index: continue
        current = int(list[i])
        if abs(current - last) > 3 or abs(current - last) < 1:
            if skip_index == -1 and (issafe(list, i) or issafe(list, i-1)): return True
            return False
        currentsign = 1 if current - last > 0 else -1
        if sign != 0 and currentsign != sign:
            if skip_index == -1 and (issafe(list, i) or issafe(list, i-1)): return True
            return False
        sign = currentsign
        last = current
    return True

with open("inputs/day2.txt") as f:
    lines = f.readlines()

sum = 0
for line in lines:
    split = line.split()
    safe = issafe(split) or issafe(split, 0)
    if safe: sum += 1

print(sum)