with open('inputs/day9.txt') as f:
	compacted = f.readline().strip()

# expand the filesystem representation
fs = []
empty = False
i = 0
for c in compacted:
	fs.extend([None if empty else i] * int(c))
	if empty:
		empty = False
	else:
		empty = True
		i += 1

# defragment file system
while None in fs:
	last = fs[-1]
	fs[fs.index(None)] = last
	fs = fs[:-1]
	
# calculate checksum
print(sum([pos * block for pos, block in enumerate(fs)]))