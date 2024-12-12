DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# read file
with open('inputs/day12.txt') as f:
	plantmap = [line.strip() for line in f.readlines()]
height = len(plantmap)
width = len(plantmap[0])

# determine regions
regions = []
def findregion(plantmap, region, x, y):
	# validate if this is point is even valid, saves logic elsewere
	if any((x, y) in region for region in regions) or (x, y) in region: return
	region.add((x, y))
	for xOff, yOff in DIRECTIONS:
		if x+xOff < 0 or y+yOff < 0 or x+xOff >= width or y+yOff >= height: continue
		if plantmap[y][x] == plantmap[y+yOff][x+xOff]:
			findregion(plantmap, region, x+xOff, y+yOff)

for x in range(width):
	for y in range(height):
		region = set()
		findregion(plantmap, region, x, y)
		if len(region) > 0 and region not in regions:
			regions.append(region)

# calculate price
price = 0
for region in regions:
	area = len(region)
	sides = 0
	visited = set()
	for plot in region:
		for side in DIRECTIONS:
			if (plot[0] + side[0], plot[1] + side[1]) in region or (plot, side) in visited: continue
			sides += 1 # count this side
			# mark all other plants on this side as visited
			for dir in DIRECTIONS:
				if abs(side[0]) == abs(dir[0]) and abs(side[1])==abs(dir[1]): continue # make sure that dir has a 90 degree andgle to side 
				x, y = plot
				while (x, y) in region and (x+side[0], y+side[1]) not in region:
					visited.add(((x, y), side))
					x, y = x+dir[0], y+dir[1]
	price += area * sides
print(price)