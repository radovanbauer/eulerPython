from time import perf_counter
from primesieve import primes
time1 = perf_counter()

# S(p**k) = (2*k + 1) * S(1)
# S(p * n) = 3 * S(n)
# S(p**k * n) = (2*k + 1) * S(n)
# S(product(p_i ** a_i)) = product(2*a_i + 1)

N = 10**7
MOD = 1000000087

primes = primes(N + 1)

spf = (N + 1) * [0]
for p in primes:
    for k in range(1, N // p + 1):
        if spf[p * k] == 0:
            spf[p * k] = p

def factorint(n):
    res = {}
    while n > 1:
        p = spf[n]
        e = 1
        n //= p
        while n % p == 0:
            n //= p
            e += 1
        res[p] = e
    return res

prod = factorint(1)
s = 1
res = 0
for n in range(2, N + 1):
    for p, e in factorint(n).items():
        prev_e = prod.get(p, 0)
        prod[p] = prev_e + e
        s = s * (2*prod[p] + 1) * pow(2*prev_e + 1, -1, MOD) % MOD
    if n % 1000 == 0:
        print(f"{n=} {s=}")
    res = (res + s) % MOD
print(res)

time2 = perf_counter()
print(time2 - time1)