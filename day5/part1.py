def is_correct(update: list[int], rules: list[(int, int)]):
    for i in range(len(update)):
        page = update[i]
        if any(after in update[:i] for (first, after) in rules if first == page): return False
    return True

rules = []
updates = []
with open('inputs/day5.txt') as f:
    while True:
        line = f.readline().split('|')
        if len(line) == 1: break
        rules.append((int(line[0]), int(line[1])))
    
    updates = [[int(page) for page in line.split(',')] for line in f.readlines()]

res = sum(update[len(update)//2] for update in updates if is_correct(update, rules))

print(res)