list1, list2 = [], []
with open("inputs/day1.txt") as f:
    for line in f.readlines():
        split = line.split()
        list1.append(int(split[0]))
        list2.append(int(split[-1]))

sum = 0
for item in list1:
    sum += item * len([x for x in list2 if x == item])

print(sum)