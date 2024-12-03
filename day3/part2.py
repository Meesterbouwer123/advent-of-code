import re

p = re.compile('mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)')

with open('inputs/day3.txt') as f:
    data = f.read()

sum = 0
pos = 0
enabled = True
while True:
    match = p.search(data, pos)
    if match == None: break
    
    if data[match.start():match.end()] == "do()":
        enabled = True
    elif data[match.start():match.end()] == "don't()":
        enabled = False
    elif enabled:
        sum += int(match.group(1)) * int(match.group(2))
        
    pos = match.end()

print(sum)