# parse file
machines = []
import re
with open('inputs/day13.txt') as f:
	data = f.read()
	for match in re.findall('Button A\: X\+(\d+), Y\+(\d+)\nButton B\: X\+(\d+), Y\+(\d+)\nPrize\: X\=(\d+), Y\=(\d+)', data):
		machines.append([(int(match[0]), int(match[1])), (int(match[2]), int(match[3])), (int(match[4]), int(match[5]))])

def find_solution(a, b, prize):
	score = None
	for i in range(100):
		for j in range(100):
			pos = (i*a[0] + j*b[0], i*a[1] + j*b[1])
			if pos != prize: continue
			if score == None or 3*i + j < score: score = 3*i + j
	return score

sum = 0
for (a, b, prize) in machines:
	cost = find_solution(a, b, prize)
	if cost != None: sum += cost
print(sum)