from bisect import bisect_right
from math import floor, log
from primesieve import primes

Nlog = 800800 * log(800800)
Nlog2 = Nlog / log(2)
primes = primes(floor(Nlog2))

count = 0

for pi in range(len(primes)):
    p = primes[pi]
    idx = bisect_right(primes, Nlog, key=lambda q: q * log(p) + p * log(q))
    qcount = max(0, idx - pi - 1)
    if qcount == 0:
        break
    count += qcount

print(count)
