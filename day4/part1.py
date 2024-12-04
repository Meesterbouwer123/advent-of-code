with open('inputs/day4.txt') as f:
    horizontals = [line.strip() for line in f.readlines()]

width = len(horizontals[0])
height = len(horizontals)

verticals = ["".join([horizontals[y][x] for y in range(height) if x < len(horizontals[y])]) for x in range(width)]
diagonals1 = {}
diagonals2 = {}
for x in range(width):
    for y in range(height):
        # some lines dont have the newline, making them shorter
        if x >= len(horizontals[y]): continue 

        if x-y in diagonals1:
            diagonals1[x - y] += horizontals[y][x]
        else:
            diagonals1[x-y] = horizontals[y][x]
        
        if width*height-x-y in diagonals2:
            diagonals2[width*height-x-y] += horizontals[y][x]
        else:
            diagonals2[width*height-x-y] = horizontals[y][x]

res = 0
for set in [horizontals, verticals, diagonals1.values(), diagonals2.values()]:
    res += sum([line.count('XMAS') for line in set]) + sum([line.count('SAMX') for line in set])

print(res)