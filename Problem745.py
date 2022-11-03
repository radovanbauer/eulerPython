from functools import cache
from math import floor, sqrt


def max_square(n):
    nsqrt = floor(sqrt(n))
    for d in range(nsqrt, 0, -1):
        if (n % (d * d) == 0):
            return d * d


@cache
def sl(n):
    res = n
    d = 2
    while d * d <= n:
        res -= sl(n // (d * d))
        d += 1
    return res


def S(n):
    res = 0
    g = 1
    while g * g <= n:
        res += g * g * sl(n // (g * g))
        g += 1
    return res

print(S(10 ** 14) % 1000000007)
