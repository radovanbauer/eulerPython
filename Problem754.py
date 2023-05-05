from time import perf_counter
import primesieve
time1 = perf_counter()

N = 10**8
MOD = 1000000007

primes = primesieve.primes(N + 1)

mob = (N + 1) * [1]
for p in primes:
    for k in range(1, N // p + 1):
        mob[p * k] *= -1
    for k in range(1, N // (p ** 2) + 1):
        mob[p ** 2 * k] = 0

spf = (N + 1) * [0]
for p in primes:
    for k in range(1, N // p + 1):
        if spf[p * k] == 0:
            spf[p * k] = p

def prime_divs(n):
    res = [1]
    while n > 1:
        p = spf[n]
        ppows = [1, p]
        # ppow = p
        n //= p
        while n % p == 0:
            n //= p
            # ppow *= p
            # ppows.append(ppow)
        res = [d * ppow for d in res for ppow in ppows]
    return res

def coprime_count(n, k):
    return sum(n // d * mob[d] for d in prime_divs(k))

res = 1
for k in range(2, N + 1):
    if k % 100000 == 0:
        print(k)
    res *= pow(k, coprime_count(N, k) - coprime_count(k, k), MOD)
    res %= MOD
    # print(f"{k=} {divs(k)=}")
print(res)

time2 = perf_counter()
print(time2 - time1)