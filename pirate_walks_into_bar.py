nums = [2, 0, 1, 9]

def answer(numbers):
    pirates = []
    pirate = 0
    while True:
        if pirate in pirates:
            return len(pirates) - pirates.index(pirate)
        pirates.append(pirate)
        pirate = numbers[pirate]

print answer(nums)
