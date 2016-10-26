def answer(n):
    # Number of squares to buy
    gauzecount = 0
    # Loop while we still have money
    while n:
        i = 1               # Index
        x = 1               # Squared index
        # Build up the index into our remaining money
        while x <= n:
            x = i*i
            i += 1
        # Bring the squared number back down
        x = (i-2) * (i-2)
        # Buy the square
        n -= x
        gauzecount += 1
    return gauzecount

print answer(24)
print answer(160)
