def trabajos(rnd, trab=(5, 6, 7, 8, 9), freq=(3, 8, 9, 6, 4)):
    p = [f / sum(freq) for f in freq]
    s = [0,0,0,0,0]
    for i in range(len(s)):
        s[i] = sum(p[:i+1])
        if rnd < s[i]:
            return trab[i]


def uniforme(rnd,a = 3,b = 7):
    return a + rnd * (b - a)
