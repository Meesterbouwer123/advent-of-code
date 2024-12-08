frequencies = {}
width, height = 0, 0
with open('inputs/day8.txt') as f:
    antennas = [l.strip() for l in f.readlines()]
    for y, line in enumerate(antennas):
        height = max(y + 1, height)
        for x, char in enumerate(line):
            width = max(x + 1, width)
            if char == '.': continue
            if char in frequencies:
                frequencies[char].append((x, y))
            else:
                frequencies[char] = [(x, y)]

antinodes = set()
for frequency in frequencies:
    frequencymap = frequencies[frequency]
    for p1 in frequencymap:
        for p2 in frequencymap:
            if p1 == p2: continue
            # calculate the antinodes
            delta = (p1[0] - p2[0], p1[1] - p2[1])
            for i in range(-width, width):
                antinode = (p1[0] + i*delta[0], p1[1] + i*delta[1])
                if antinode[0] >= 0 and antinode[0] < width and antinode[1] >= 0 and antinode[1] < height:
                    antinodes.add(antinode)

print(len(antinodes))