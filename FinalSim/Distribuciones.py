def trabajos(rnd):
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
def uniforme(rnd,a = 3,b = 7):
    return a + rnd * (b - a)
