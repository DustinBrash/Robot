import math
def nCr(n, r):
    f = math.factorial
    n, r = float(n), float(r)
    return f(n) / f(r) / f(n - r)

