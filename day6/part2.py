import copy

# simulate the guard until he leaves or enters a loop
def will_loop(obstacleMap, guardX, guardY, guardDir):
    guardMap = [[set() for x in range(width)] for y in range(height)] # doing [[Flse]*width]*height makes all the columns linked for some reason

    while guardX >=0 and guardX < width and guardY >=0 and guardY < height:
        if guardDir in guardMap[guardY][guardX]: # if we reached a place we already visited, we are in a loop
            return True, guardMap
        guardMap[guardY][guardX].add(guardDir)

        # check if there is an object in front
        pathBlocked = True
        while pathBlocked:
            if guardDir == 0: # up
                pathBlocked = guardY > 0 and obstacleMap[guardY - 1][guardX]
            elif guardDir == 1: # right
                pathBlocked = guardX < width - 1 and obstacleMap[guardY][guardX + 1]
            elif guardDir == 2: # down
                pathBlocked = guardY < height - 1 and obstacleMap[guardY + 1][guardX]
            elif guardDir == 3: # left
                pathBlocked = guardX > 0 and obstacleMap[guardY][guardX - 1]
            
            if pathBlocked: guardDir = (guardDir + 1) % 4

        # move guard
        if guardDir == 0: guardY -= 1
        elif guardDir == 1: guardX += 1
        elif guardDir == 2: guardY += 1
        elif guardDir == 3: guardX -= 1
    return False, guardMap

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

import time
start = time.time()
res = 0
loops, visited = will_loop(obstaclemap, guardX, guardY, guardDir)
for y in range(height):
    for x in range(width):
        if obstaclemap[y][x] or not visited[y][x]:  # already existing obstacles or places the guard doesn't visit will be skipped
            continue
        #print(x, y)
        cloned = copy.deepcopy(obstaclemap)
        cloned[y][x] = True
        loops, _ = will_loop(cloned, guardX, guardY, guardDir)
        if loops:
            #print('found one at', x, y)
            res += 1

print(res)
print("it took %d seconds to calculate this" % (time.time() - start))