with open('inputs/day6.txt') as f:
    room = [line.rstrip() for line in f.readlines()]

height = len(room)
width = len(room[0])

obstaclemap = []
guardX, guardY = 0, 0
guardDir = 0
for y in range(height):
    thisrow = []
    for x in range(width):
        thisrow.append(room[y][x] == '#')

        if room[y][x] == "^":
            guardX, guardY = x, y
            guardDir = 0
        elif room[y][x] == ">":
            guardX, guardY = x, y
            guardDir = 1
        elif room[y][x] == "v":
            guardX, guardY = x, y
            guardDir = 2
        elif room[y][x] == "<":
            guardX, guardY = x, y
            guardDir = 3
    obstaclemap.append(thisrow)

guardMap = [[False] * width for i in range(height)]  # doing [[Flse]*width]*height makes all the columns linked for some reason

while guardX >=0 and guardX < width and guardY >=0 and guardY < height:
    guardMap[guardY][guardX] = True

    # check if there is an object in front
    if guardDir == 0: # up
        pathBlocked = guardY > 0 and obstaclemap[guardY - 1][guardX]
    elif guardDir == 1: # right
        pathBlocked = guardX < width - 1 and obstaclemap[guardY][guardX + 1]
    elif guardDir == 2: # down
        pathBlocked = guardY < height - 1 and obstaclemap[guardY + 1][guardX]
    elif guardDir == 3: # left
        pathBlocked = guardX > 0 and obstaclemap[guardY][guardX - 1]
    
    if pathBlocked: guardDir = (guardDir + 1) % 4

    # move guard
    if guardDir == 0: guardY -= 1
    elif guardDir == 1: guardX += 1
    elif guardDir == 2: guardY += 1
    elif guardDir == 3: guardX -= 1

#for y, row in enumerate(guardMap): print([('#' if obstaclemap[y][x] else ('X' if val else '.')) for x, val in enumerate(row)])
print(sum([len([pos for pos in row if pos]) for row in guardMap]))