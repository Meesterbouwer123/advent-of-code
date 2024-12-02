def issafe(list):
    last = int(list[0])
    sign = 0
    for i in range(1, len(list)):
        current = int(list[i])
        if abs(current - last) > 3 or abs(current - last) < 1: 
            return False
        currentsign = (current - last) / abs(current - last)
        if sign != 0 and currentsign != sign: 
            return False
        sign = currentsign
        last = current
    return True

with open("inputs/day2.txt") as f:
    lines = f.readlines()

sum = 0
for line in lines:
    split = line.split()
    safe = issafe(split)
    if safe: sum += 1

print(sum)