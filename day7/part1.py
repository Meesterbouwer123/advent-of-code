def can_produce(final, numbers):
    #print(final, numbers)
    if len(numbers) == 1:
        return final == numbers[0]
    return can_produce(final - numbers[-1], numbers[:-1]) or can_produce(final / numbers[-1], numbers[:-1])


with open('inputs/day7.txt') as f:
    lines = f.readlines()

calibrations = [(int(line.split(":")[0]), [int(x) for x in line.split(": ")[1].split(" ")]) for line in lines]
print(sum([final for (final, nums) in calibrations if can_produce(final, nums)]))