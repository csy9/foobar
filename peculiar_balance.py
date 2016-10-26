def answer(x):
    # Convert base 10 number to base 3
    def to_b3(n10):
        n3 = 0
        i = 1
        while n10:
            n3 += i * (n10 % 3)
            n10 /= 3
            i *= 10
        return n3

# Initialize scale sides and list of actions
left_side = [x]
right_side = []
actions = []

# Convert input to backwards list of base-three numbers
nums = [int(n) for n in str(to_b3(x))][::-1]

# Current power of three
i = 0

# Go through our ternary number digit by digit.
# Match a 0 or a 1, and "subtract" to balance a 
# 2 by adding to the left side
while sum(left_side) != sum(right_side):
    # Add to left side to carry digit forward and balance later
    if nums[i] == 2:
        actions.append('L')
        left_side.append(3 ** i)

    # Add to right side to balance digit
    elif nums[i] == 1:
        actions.append('R')
        right_side.append(3 ** i)

    # Do nothing
    else:
        actions.append('-')

    # Re-calculate our number
    nums = [int(n) for n in str(to_b3(sum(left_side)))][::-1]
    i += 1

return actions
