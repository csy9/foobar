def answer(chunk, word):
    n = len(word)
    # Recursive function to make a tree of string-splitting possibilities
    leaves = []
    visitednodes = []
    def makesplits(subchunk):
        # Base case, no more occurences of word
        if word not in subchunk:
            leaves.append(subchunk)
        # Append all leaves below this node to the leaves[] array
        else:
            # Indicies of occurences of word in subchunk
            indices = [i for i in xrange(len(subchunk)-n+1) if subchunk[i:i+n] == word]
            # All possibilities of removing instance of word from subchunk
            options = [subchunk[0:i] + subchunk[i+n:] for i in indices]
            # Try to further split each possibility before adding it to the result
            for option in options:
                if option not in visitednodes:
                    visitednodes.append(option)
                    makesplits(option)

    # Get list of possible options to choose from
    makesplits(chunk)

    # Filter out options that are too long, and return earliest lex string
    minlen = len(min(leaves, key=len))
    return min([x for x in leaves if len(x) == minlen])

print answer("lololololo", "lol")
print answer("goodgooogoogfogoood", "goo")
