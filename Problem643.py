from sympy import sieve
from math import isqrt
from time import perf_counter
from functools import cache
time1 = perf_counter()

N = 10**11
MOD = 1000000007
mobius = [0] + list(sieve.mobiusrange(1, isqrt(N) + 2))
print(len(mobius))

def coprime_count(n):
    res = 0
    D = isqrt(n)
    for d in range(1, D + 1):
        res += mobius[d] * (n // d) ** 2
    for e in range(n // D - 1, 0, -1):
        dmin = n // (e + 1) + 1
        dmax = n // e
        if dmax < dmin:
            continue
        print(f"{n=} {e=} {dmin=} {dmax=}")
        assert n // dmin == e
        # assert n // (dmin - 1) > e
        # assert n // dmax == e
        # assert n // (dmax + 1) < e
        # res += sum(mobius[d] for d in range(dmin, dmax + 1)) * e ** 2
        res += (M(dmax) - M(dmin - 1)) * e ** 2
    return res

@cache
def M(n):
    if n == 0:
        return 0
    # if n == 1:
    #     return 1
    res = 1
    D = isqrt(n)
    for x in range(2, D + 1):
        res -= M(n // x)
    for e in range(n // D - 1, 0, -1):
        dmin = n // (e + 1) + 1
        dmax = n // e
        if dmax < dmin:
            continue
        res -= (dmax - dmin + 1) * M(e)
    return res

def f(n):
    sum = 0
    pow2 = 2
    while pow2 <= n:
        sum += (coprime_count(n // pow2) - 1) // 2
        pow2 *= 2
    return sum

print(f(N) % MOD)

# print([M(n) for n in range(0, 11)])

time2 = perf_counter()
print(time2 - time1)