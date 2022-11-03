from functools import cache
from math import floor, sqrt
import primesieve
import sympy
import sys
sys.setrecursionlimit(100000)

N = 10**10
primes = primesieve.primes(floor(sqrt(N)))


@cache
def count(max_pi, max_prod):
    if max_pi < 0:
        return 1 if max_prod >= 1 else 0
    res = 0
    ppow = 1
    while ppow <= max_prod:
        x = count(max_pi - 1, max_prod // ppow)
        res += x
        ppow *= primes[max_pi]
    return res


res1 = sum(count(pi, N // p**2) - 1 for pi, p in enumerate(primes))
res2 = sum(count(pi - 1, N // p) - count(pi - 1, p) for pi, p in enumerate(primes) if N // p >= pi)
print(res1 + res2 + 1)
