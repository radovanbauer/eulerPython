# Sp(N, p) = (N - N // p) * ((N // p - N // p**2) * 1 + (N // p**2 - N // p**3) * 2 + ...)
#          + (N // p - N // p**2) * ((N // p**2 - N // p**3) * 1 + (N // p**3 - N // p**4) * 2 + ...)
#
# Sp(N, p) = (N - N // p) * sum(N // p**k, k, 1, ...)
#          + (N // p - N // p**2) * sum(N // p**k, k, 2, ...)
#
# Sp(N, p) = N * sum(N // p**k, k, 1, ...) - sum((N // p**k) ** 2, k, 1, ...)

import primesieve
from time import perf_counter
from math import sqrt, floor
time1 = perf_counter()

N = 10**12
MOD = 1000000007

def Sp(N, p):
    res = 0
    ppow = p
    while ppow <= N:
        res += N * (N // ppow) - (N // ppow) ** 2
        ppow *= p
    return res

Ns = floor(sqrt(N))
assert Ns ** 2 == N
primes = primesieve.primes(Ns)
sum = 0

for p in primes:
    x = Sp(N, p)
    sum += x
    print(f"{p=} {Sp(N, p)=}")

for k in range(Ns, 1, -1):
    a = N // k + 1
    b = (N // (k - 1))
    prime_count = primesieve.count_primes(a, b)
    print(f"{a=} {b=} {prime_count=}")
    assert N // a == N // b, f"{N // a}  {N //b}"
    sum += prime_count * Sp(N, a)

print(sum*2 % MOD)

time2 = perf_counter()
print(time2 - time1)
