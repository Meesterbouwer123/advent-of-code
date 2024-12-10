def trailhead_rating(trailmap, x, y):
	height = len(trailmap)
	width = len(trailmap[0])
	score = 0
	val = trailmap[y][x]
	if val == 9: return 1
	for (offX, offY) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
		if x+offX >= 0 and x + offX < width and y+offY >= 0 and y+offY < height:
			if trailmap[y+offY][x+offX] != val + 1: continue
			score += trailhead_rating(trailmap, x+offX, y+offY)
	return score

with open('inputs/day10.txt') as f:
	trailmap = [[int(c) for c in line.strip()] for line in f.readlines()]

score = 0
for y, row in enumerate(trailmap):
	for x, c in enumerate(row):
		if c==0:
			tscore = trailhead_rating(trailmap, x, y)
			score += tscore
print(score)