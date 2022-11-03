import sympy
from time import perf_counter
time1 = perf_counter()

# N = 16
# N = 100
# N = 10000
N = 10**18

primes = list(sympy.ntheory.sieve.primerange(10**6))

def cubefulls(n, minpi, maxpi):
    if maxpi - minpi <= 0:
        return []
    if maxpi - minpi == 1:
        x = primes[minpi] ** 3
        res = [1]
        while x <= n:
            res.append(x)
            x *= primes[minpi]
        return res
    mid = (minpi + maxpi) // 2
    c1 = cubefulls(n, minpi, mid)
    c2 = cubefulls(n, mid, maxpi)
    res = []
    for x in c1:
        for y in c2:
            if x * y <= n:
                res.append(x * y)
            else:
                break
    res.sort()
    return res

print(sum(N // c for c in cubefulls(N, 0, len(primes))))

time2 = perf_counter()
print(time2 - time1)