def answer(food, grid):
    # Length of grid
    N = len(grid)

    # Table of calls to walk() to remember
    cache = {}

    # Walk backwards through the zombie maze
    def walk(f, r, c):
        call = (f, r, c)
        # Deja Vu
        if call in cache:
            return cache[call]
        # Uncharted territory
        else:
            # Default to a value that will indicate the path is invalid
            result = food+1

            # Feed the zombie
            f -= grid[r][c]

            # Base case; we made it through the maze!
            if r == c == 0:
                result = f
            # Still have work to do. Try moving up + left
            elif f >= 0:
                up = left = result
                if r:
                    up = walk(f, r-1, c)
                if c:
                    left = walk(f, r, c-1)
                result = min(up, left)

            # Drop a breadcrumb and march onwards
            cache[call] = result
            return result

    f = walk(food, N-1, N-1)
    return f if f < food else -1

g = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
h = [[x*y for x in range(20)] for y in range(20)]
print answer(7, g)
print answer(12, g)
print answer(10000, h)
