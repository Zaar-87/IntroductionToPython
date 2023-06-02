def LastFibon(n):
    if n in [1, 2]:
        return n
    return LastFibon(n - 1) + LastFibon(n - 2)