def is_correct(update: list[int], rules: list[(int, int)]):
    for i in range(len(update)):
        page = update[i]
        if any(after in update[:i] for (first, after) in rules if first == page): return False
    return True

def fix_update(update: list[int], rules: list[(int, int)]):
    if is_correct(update, rules):
        return update
    
    did_change = False
    for i in range(len(update)):
        for j in range(i, len(update)):
            # if 2 are out of order, swap them
            if (update[j], update[i]) in rules:
                update[j], update[i] = update[i], update[j]
                did_change = True
    
    if not did_change:
        raise "nothing changed!"
    
    # recursion here because i don't want to do a while loop around the other two loops
    return fix_update(update, rules)

rules = []
updates = []
with open('inputs/day5.txt') as f:
    while True:
        line = f.readline().split('|')
        if len(line) == 1: break
        rules.append((int(line[0]), int(line[1])))
    
    updates = [[int(page) for page in line.split(',')] for line in f.readlines()]

res = 0

for update in updates:
    if not is_correct(update, rules):
        fixed = fix_update(update, rules)
        res += fixed[len(fixed)//2]

print(res)