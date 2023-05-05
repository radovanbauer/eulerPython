from primesieve import primes
from functools import reduce
from sympy import divisors
from time import perf_counter
from functools import cache
time1 = perf_counter()

MOD = 1000000007

def G(n):
    ps = primes(n)
    for p in ps:
        for c in str(p):
            if c != "0":
                yield int(c)

@cache
def divs(n):
    return divisors(n)

def F(n):
    all_count = 1#reduce(lambda a, b: a * b % MOD, map(lambda c: len(divs(int(c))), str))
    res = 0
    prev_count = [0 for d in range(0, 10)]
    i = 0
    for c in G(n):
        if i % 1000 == 0:
            print(i)
        divs2 = divs(c)
        for c1 in range(0, 10):
            divs1 = divs(c1)
            for d1 in divs1:
                for d2 in divs2:
                    if d1 > d2:
                        res = (res + prev_count[c1] * pow(len(divs1) * len(divs2), -1, MOD)) % MOD
        prev_count[c] += 1
        all_count = (all_count * len(divs2)) % MOD
        i += 1
    return res * all_count % MOD

print(F(10**8))

time2 = perf_counter()
print(time2 - time1)