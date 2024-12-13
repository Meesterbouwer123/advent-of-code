# parse file
machines = []
import re, z3
with open('inputs/day13.txt') as f:
	data = f.read()
	for match in re.findall('Button A\: X\+(\d+), Y\+(\d+)\nButton B\: X\+(\d+), Y\+(\d+)\nPrize\: X\=(\d+), Y\=(\d+)', data):
		machines.append([(int(match[0]), int(match[1])), (int(match[2]), int(match[3])), (int(match[4])+10000000000000, int(match[5])+10000000000000)])

def find_solution(a, b, prize):
	# solve using z3
	i, j = z3.Int('i'), z3.Int('j')
	s = z3.Optimize()
	s.add(z3.And(i*a[0] + j*b[0] == prize[0], i*a[1] + j*b[1] == prize[1]))
	s.minimize(3*i+j)
	if s.check() == z3.unsat: return None
	m = s.model()
	print(m)
	return m.eval(3*i+j).as_long()

sum = 0
for (a, b, prize) in machines:
	cost = find_solution(a, b, prize)
	if cost != None: sum += cost
print(sum)