#!/usr/bin/python2

def answer(t, n):

    cache = {}

    def play(rolls, place):
        # Memoize calls
        call = (rolls, place)
        if call in cache:
            return cache[call]

        # Out of moves or off the board
        if rolls > t or place > n or place < 1:
            val = 0

        # Reached the end, only need to roll stay's
        elif place == n:
            val = 1

        # Play out the other options
        else:
            val = play(rolls+1, place) + play(rolls+1, place-1) + play(rolls+1, place+1)

        cache[call] = val
        return val % 123454321

    return play(0, 1)

print answer(1, 2)
print answer(3, 2)
print answer(500, 400)
