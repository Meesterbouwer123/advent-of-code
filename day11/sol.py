import math

cache = {}

def solve(num, depth):
	# recursion base case
	if depth == 0: return 1
	
	# check if we already calculated this, speeds things up ***A LOT***
	if num in cache:
		if depth in cache[num]: return cache[num][depth]
	else: cache[num] = {}

	if num == 0:
		res = solve(1, depth -1)
		cache[num][depth] = res
		return res
	elif math.floor(math.log(num, 10)) % 2 == 1:
		# split num
		x = 10**(math.floor(math.log(num, 10)) // 2 + 1)
		first, second = num //x, num % x
		res = solve(first, depth - 1) + solve(second, depth -1)
		cache[num][depth] = res
		return res
	else:
		res = solve(num * 2024, depth -1)
		cache[num][depth] = res
		return res
		
# read file
with open("inputs/day11.txt") as f:
	stones = [int(x) for x in f.readline().strip().split(" ")]

# print solutions
print('p1:', sum(solve(stone, 25) for stone in stones))
print('p2:', sum(solve(stone, 75) for stone in stones))