list1, list2 = [], []
with open("inputs/day1.txt") as f:
    for line in f.readlines():
        split = line.split()
        list1.append(int(split[0]))
        list2.append(int(split[-1]))

list1.sort()
list2.sort()

sum = 0
for i in range(len(list1)):
    sum += abs(list1[i] - list2[i])

print(sum)