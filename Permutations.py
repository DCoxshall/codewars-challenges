from itertools import permutations as pt

def permutations(string):
    return list(set([''.join(i) for i in pt(list(string))]))
