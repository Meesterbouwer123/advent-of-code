with open('inputs/day4.txt') as f:
    horizontals = [line.strip() for line in f.readlines()]

width = len(horizontals[0])
height = len(horizontals)
sum = 0
for x in range(1, width -1):
    for y in range(1, height -1):
        # for an X-MAS the center piece must be an A, with MMSS on the corners
        if horizontals[y][x] != 'A': continue
        corners = [horizontals[y - 1][x - 1], horizontals[y - 1][x + 1], horizontals[y + 1][x + 1], horizontals[y + 1][x - 1]]
        for i in range(len(corners)):
            if corners[i] == 'M' and corners[(i+1)%len(corners)] == 'M' and corners[(i+2)%len(corners)] == 'S' and corners[(i+3)%len(corners)] == 'S':
                sum += 1

print(sum)