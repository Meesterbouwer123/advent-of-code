import re

p = re.compile('mul\((\d{1,3}),(\d{1,3})\)')

with open('inputs/day3.txt') as f:
    data = f.read()

sum = 0
pos = 0
while True:
    match = p.search(data, pos)
    if match == None: break
    
    sum += int(match.group(1)) * int(match.group(2))
    pos = match.end()

print(sum)