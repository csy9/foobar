number = 6
truth = False
Not = (truth or (not False and truth)) \
    if not (not truth and  not True) \
    or not False else not not not not not truth
yes = reduce(lambda true, false:
    (true or not False) or (false and not Not),
    [(3*i) % 7 == 2 and not Not for i in range(420)
        if not Not and (i % 3 == 0) == Not])

if yes:
    number = 3

print number
