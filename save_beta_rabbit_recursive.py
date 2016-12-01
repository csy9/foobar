def answer(food, grid):
    # List to hold the remaining food in each path
    options = []

    # Recursively find weights of paths through the grid by branching at each
    # node, adding the current node to each branch.
    def findpaths(n, subgrid):
        # We've gone too far for it to be worth continuing
        if n > food:
            return

        w = food + 1
        # We are on the last row
        if len(subgrid) == 1:
            w = n + sum(subgrid[0])
        # We are on the last column
        elif len(subgrid[0]) == 1:
            w = n + sum([x[0] for x in subgrid])
        # Still have work to do
        else:
            # Add current node to current total
            n += subgrid[0][0]
            # Hang a louie (remove first column from subgrid)
            findpaths(n, [x[1:] for x in subgrid])
            # Make a right (remove first row from subgrid)
            findpaths(n, subgrid[1:])

        if w <= food:
            options.append(food - w)

    # Get list of weights of possible path options
    findpaths(0, grid)

    return min(options) if options else -1

board1 = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
board2 = [[x+y for x in range(15)] for y in range(15)]
print answer(7, board1)
print answer(12, board1)
print answer(400, board2)
