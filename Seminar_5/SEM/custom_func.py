def last_fibon(n):
    if n in [1, 2]:
        return n
    return last_fibon(n - 1) + last_fibon(n - 2)