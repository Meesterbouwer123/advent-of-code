# read file
with open('inputs/day12.txt') as f:
	plantmap = [line.strip() for line in f.readlines()]
height = len(plantmap)
width = len(plantmap[0])

# determine regions
regions = []
def findregion(plantmap, region, x, y):
	# validate if this is point is even valid, saves logic elsewere
	if any(r for r in regions if r==(x, y)) or (x, y) in region: return
	region.add((x, y))
	for xOff, yOff in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
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
	perimiter = 0
	for plot in region:
		for xOff, yOff in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
			if (plot[0] + xOff, plot[1] + yOff) not in region: perimiter += 1
	price += area * perimiter
print(price)