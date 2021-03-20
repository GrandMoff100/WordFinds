import random


def filler():
    weights = {
        'E': 13,
        'T': 9,
        'A': 8,
        'O': 8,
        'N': 7,
        'I': 7,
        'S': 6,
        'R': 6,
        'H': 6,
        'L': 4,
        'D': 4,
        'U': 3,
        'C': 3,
        'M': 2,
        'F': 2,
        'W': 2,
        'G': 2,
        'P': 2,
        'Y': 2,
        'B': 2,
        'V': 1,
        'K': 1,
        'X': 1,
        'J': 1,
        'Q': 1,
        'Z': 1
    }
    return random.choice(''.join([k*v for k,v in weights.items()])).upper()


def rrange(*args):
    args = list(args)
    args.sort()
    a, b, *_ = args
    return range(a,b+1)

