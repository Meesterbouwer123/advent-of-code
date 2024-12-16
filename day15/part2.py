with open('inputs/day15.txt') as f:
    rawmap, moves = f.read().split('\n\n')

a = {
    0: '.',
    1: '[',
    2: ']',
    -1: '#'
}
def test(om):
    for y, l in enumerate(om):
        for x, c in enumerate(l):
            if (c == 1 and om[y][x+1] != 2) or (c == 2 and om[y][x-1] != 1):
                print("invalid object map!", x, y)
                print('\n'.join(''.join(('@' if x==botX and y==botY else a[c]) for x, c in enumerate(line)) for y, line in enumerate(obstaclemap)))
                return False
    return True

# parse map
obstaclemap = []
botX, botY = 0, 0
for y, line in enumerate(rawmap.split('\n')):
    row = []
    for x, char in enumerate(line.strip()):
        if char == '#':
            row.extend([-1, -1])
        elif char == 'O':
            row.extend([1, 2])
        else:
            row.extend([0, 0])
        
        if char == '@':
            botX, botY = x*2, y
    obstaclemap.append(row)

# make all the moves
directions = {
    '>': (1, 0),
    '<': (-1, 0),
    '^': (0, -1),
    'v': (0, 1),
}
#print('\n'.join(''.join(('@' if x==botX and y==botY else a[c]) for x, c in enumerate(line)) for y, line in enumerate(obstaclemap)))
for move in moves.strip():
    if move not in directions: continue
    dir = directions[move]
    print(move)
    todo = [(botX + dir[0], botY + dir[1])]
    shouldpush = []
    canpush = True
    while len(todo) > 0:
        (x, y) = todo.pop()
        if obstaclemap[y][x] == -1: # wall = no movement
            canpush = False
            break
        elif obstaclemap[y][x] == 1: # left side of block
            if (x + dir[0], y + dir[1]) not in shouldpush and (x + dir[0], y + dir[1]) not in todo: todo.append((x + dir[0], y + dir[1])) # the area in front
            if (x + dir[0]+1, y + dir[1]) not in shouldpush and (x + dir[0]+1, y + dir[1]) not in todo: todo.append((x + dir[0] + 1, y + dir[1])) # the area in front of the other half
            if (x, y) not in shouldpush: shouldpush.append((x, y))
            if (x+1, y) not in shouldpush: shouldpush.append((x+1, y))
        elif obstaclemap[y][x] == 2: # right side of block
            if (x + dir[0] -1, y + dir[1]) not in shouldpush and (x + dir[0]-1, y + dir[1]) not in todo: todo.append((x + dir[0] - 1, y + dir[1])) # the area in front of the other half
            if (x + dir[0], y + dir[1]) not in shouldpush and (x + dir[0], y + dir[1]) not in todo: todo.append((x + dir[0], y + dir[1])) # the area in front
            if (x, y) not in shouldpush: shouldpush.append((x, y))
            if (x-1, y) not in shouldpush: shouldpush.append((x-1, y))
            
    if canpush:
        print('moving %d tiles' % len(shouldpush), shouldpush)
        shouldpush.reverse()
        for (x, y) in shouldpush:
            # the one in front should be empty, overwrite it
            obstaclemap[y+dir[1]][x+dir[0]] = obstaclemap[y][x]
            if (x-dir[0],y-dir[1]) not in shouldpush: obstaclemap[y][x] = 0 # if there is nothing that could overwrite this, set this space to empty
        botX, botY = botX + dir[0], botY + dir[1]
    if not test(obstaclemap): break
    print('\n'.join(''.join(('@' if x==botX and y==botY else a[c]) for x, c in enumerate(line)) for y, line in enumerate(obstaclemap)))


print('\n'.join(''.join(a[x] for x in line) for line in obstaclemap))

res = 0
for y, row in enumerate(obstaclemap):
    for x, state in enumerate(row):
        if state == 1: # left side of box here
            res += 100 * y + x

print(res)