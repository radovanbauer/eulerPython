import sympy
from time import perf_counter
time1 = perf_counter()

N = 20000
MOD = 1000000007


def addfactors(target: dict, source: dict, mul=1):
    for p, e in source.items():
        target[p] = target.get(p, 0) + e*mul


sum = 0
factors = {}
factorfact = {}
for n in range(1, N + 1):
    print(n)
    addfactors(factors, sympy.ntheory.factorint(n), mul=n - 1)
    if n > 1:
        addfactors(factorfact, sympy.ntheory.factorint(n - 1))
        addfactors(factors, factorfact, mul=-1)
    sigma = 1
    for p, e in factors.items():
        sigma *= (pow(p, e + 1, MOD) - 1) * pow(p - 1, -1, MOD)
    sum += sigma % MOD
print(sum % MOD)

time2 = perf_counter()
print(time2 - time1)
