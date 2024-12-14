# parse file
import re
robots = []
with open('inputs/day14.txt') as f:
	data = f.read()
	for match in re.findall('p\=(\d+),(\d+) v\=(-?\d+),(-?\d+)', data):
		robots.append(([int(match[0]), int(match[1])], (int(match[2]), int(match[3]))))
	width = 101
	height = 103

print(robots)

# simulate 100 seconds of movement
for _ in range(100):
	for i in range(len(robots)):
		pos = robots[i][0]
		velocity = robots[i][1]
		pos[0] = (pos[0] + velocity[0]) % width
		if pos[0] < 0: pos[0] += width
		pos[1] = (pos[1] + velocity[1]) % height
		if pos[1] < 0: pos[1] += height

# calculate safety score
quadrants = [0] * 4
for (pos, _) in robots:
	if pos[0] < width // 2 and pos [1] < height // 2:
		quadrants[0] += 1
	elif pos[0] > width // 2 and pos [1] < height // 2:
		quadrants[1] += 1
	elif pos[0] < width // 2 and pos [1] > height // 2:
		quadrants[2] += 1
	elif pos[0] > width // 2 and pos [1] > height // 2:
		quadrants[3] += 1
sf = 1
for quadrant in quadrants: sf *= quadrant
print(sf)