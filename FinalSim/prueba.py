import numpy as np


def trabajos(rnd, trab=(5, 6, 7, 8, 9), freq=(3, 8, 9, 6, 4)):
    p = [i / np.sum(freq) for i in freq]

    s = [0,0,0,0,0]
    for i in range(len(s)):
        s[i] = np.sum(p[:i+1])
        if rnd < s[i]:
            return trab[i]

def trabajos2(rnd):
    if rnd < 0.1:
        return 5
    elif rnd < 8/30+0.1:
        return 6
    elif rnd < 8/30+0.4:
        return 7
    elif rnd < 8/30+0.6:
        return 8
    elif rnd < 8/30+0.6+4/30:
        return 9

