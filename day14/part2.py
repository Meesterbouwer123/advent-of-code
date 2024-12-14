# I took another persons solution for part 2 today, this is why you spoiler your solutions when talking about AoC

# parse file
import re
robots = []
with open('inputs/day14.txt') as f:
	data = f.read()
	for match in re.findall('p\=(\d+),(\d+) v\=(-?\d+),(-?\d+)', data):
		robots.append(([int(match[0]), int(match[1])], (int(match[2]), int(match[3]))))
	width = 101
	height = 103

# simulate until the easter egg shows up
t = 0
while True:
	t += 1
	for i in range(len(robots)):
		pos = robots[i][0]
		velocity = robots[i][1]
		pos[0] = (pos[0] + velocity[0]) % width
		if pos[0] < 0: pos[0] += width
		pos[1] = (pos[1] + velocity[1]) % height
		if pos[1] < 0: pos[1] += height
	if len(set((x, y) for ((x, y), vel) in robots)) == len(robots): break # there should be no overlap if they arrange correctly

# print screen
for y in range(height):
	for x in range(width):
		a = len([robot for robot in robots if robot[0] == [x, y]])
		print(a if a != 0 else '.', end='')
	print()

print(t)