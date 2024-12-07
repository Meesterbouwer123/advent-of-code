def can_produce(final, numbers):
    #print(final, numbers)
    # check if the final one matches
    if len(numbers) == 1:
        return final == numbers[0]
    

    if final % numbers[-1] == 0 and can_produce(final // numbers[-1], numbers[:-1]): # amke suer it's divisible first, else we need to handle floating point nubmers
        return True
    
    if final >= numbers[-1] and can_produce(final - numbers[-1], numbers[:-1]):
        return True
    
    if str(final).endswith(str(numbers[-1])):
        # check if concatenation works
        stripped = str(final).removesuffix(str(numbers[-1]))
        if stripped != '' and can_produce(int(stripped), numbers[:-1]): return True
    
    return False

import time
start = time.time() * 1000

with open('inputs/day7.txt') as f:
    lines = f.readlines()

calibrations = [(int(line.split(":")[0]), [int(x) for x in line.split(": ")[1].split(" ")]) for line in lines]
print(sum([final for (final, nums) in calibrations if can_produce(final, nums)]))
print("solved in %d milliseconds" %(time.time()*1000 - start))