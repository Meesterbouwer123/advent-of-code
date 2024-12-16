with open('inputs/day15.txt') as f:
    rawmap, moves = f.read().split('\n\n')

# parse map
obstaclemap = []
botX, botY = 0, 0
for y, line in enumerate(rawmap.split('\n')):
    row = []
    for x, char in enumerate(line.strip()):
        if char == '#':
            row.append(True)
        elif char == 'O':
            row.append(False)
        else:
            row.append(None)
        
        if char == '@':
            botX, botY = x, y
    obstaclemap.append(row)

# make all the moves
directions = {
    '>': (1, 0),
    '<': (-1, 0),
    '^': (0, -1),
    'v': (0, 1),
}
for move in moves.strip():
    if move not in directions: continue
    dir = directions[move]
    posX, posY = botX + dir[0], botY + dir[1]
    while obstaclemap[posY][posX] == False:
        posX, posY = posX + dir[0], posY + dir[1]
    if obstaclemap[posY][posX] == None:
        # we can make the move
        # walk back to move all the boxes
        #print('\n'.join(''.join(('#' if state else ('O' if state == False else ' ')) for state in row) for row in obstaclemap))
        while posX != botX or posY != botY:
            obstaclemap[posY][posX] = obstaclemap[posY - dir[1]][posX - dir[0]]
            posX, posY = posX - dir[0], posY - dir[1]
        botX, botY = botX + dir[0], botY + dir[1]

res = 0
for y, row in enumerate(obstaclemap):
    for x, state in enumerate(row):
        if state == False: # box here
            res += 100 * y + x

print(res)