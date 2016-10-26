def answer(names):
    # Convert a character to its ordinal value (a:1, b:2....z:26)
    cval = lambda c: ord(c) - ord('a') + 1
    # Convert a word to the sum of its characters' ordinal values
    nval = lambda s: sum([cval(c) for c in s])

    # Get each name's ordinal value, and pair them up
    scores = [nval(n) for n in names]
    namevalpairs = zip(names, scores)

    # Group by sorted ordinal values
    scores = sorted(list(set(scores)), reverse=True)
    grouped = [[p for p in namevalpairs if p[1] == score] for score in scores]

    # Sort each sublist by name
    getname = lambda n: n[0]
    namesorted = [sorted(c, key=getname, reverse=True) for c in grouped]

    # Flatten and return the list
    return [name[0] for scoreclass in namesorted for name in scoreclass]

print answer(["annie", "bonnie", 'eeeeeeeeeeed', "liz", "al", "cj"])
