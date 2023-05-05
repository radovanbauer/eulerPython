from primesieve import primes
from math import isqrt
from time import perf_counter
time1 = perf_counter()

N = 50
MAX = 100000000
ps = primes(MAX)
ps_set = set(ps)
found = set()
res = 0
for p in ps:
    qsq = int(str(p**2)[::-1])
    q = isqrt(qsq)
    if p != q and q**2 == qsq and q in ps_set:
        found.add(p)
        res += p**2
        print(f"{p=} {q=} {p**2=} {q**2=}")
        if len(found) == N:
            break
print(f"{len(found)=} {res}")

time2 = perf_counter()
print(time2 - time1)