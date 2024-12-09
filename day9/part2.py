with open('inputs/day9.txt') as f:
	compacted = f.readline().strip()

import time
start = time.time()
# expand the filesystem representation
fs = []
files = {}
empty = False
i = 0
for c in compacted:
	fs.extend([None if empty else i] * int(c))
	if empty:
		empty = False
	else:
		empty = True
		files[i] = int(c)
		i += 1

# defragment file system
for file in range(max(files.keys()), 0, -1):
	filesize = files[file]
	start = fs.index(file)
	for i in range(start):
		if all(fs[i+offset] == None for offset in range(filesize)):
			fs = fs[:i] + fs[start:start+filesize] + fs[i+filesize:start] + fs[i:i+filesize] + fs[start+filesize:]
			break
	
# calculate checksum
print(sum([pos * block for pos, block in enumerate(fs) if block != None]))
print(f"done in %d seconds" % (time.time() - start))