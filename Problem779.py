from itertools import count
from math import floor, sqrt
import sympy
import primesieve

def f(K, n):
    factors = sympy.factorint(n)
    p = min(factors.keys())
    a = factors[p]
    return (a - 1) / (p ** K)

# 1/p / (1 - 1/p)
# p / (p * (p - 1)) = 1 / (p - 1)

def f_lim(K):
    N = 2**20
    prev_res2 = 0
    while True:
        primes = primesieve.primes(floor(sqrt(N + 1)))
        if primes[-1] ** 2 > N:
            primes.pop()
        res = 0
        for pi, p in enumerate(primes):
            # print(f"{N=} {p=}")
            ppow = p * p
            sum_nom = 0
            while ppow <= N:
                sum_nom += N // ppow
                for mobius, factor in small_prime_factors(N // ppow, primes, 0, pi):
                    sum_nom += mobius * N // (ppow * factor)
                ppow *= p
            res += sum_nom / (p - 1)
        res2 = res / N
        print(f"{N=} {res2=} {res2 - prev_res2}")
        prev_res2 = res2
        N *= 2

def small_prime_factors(N, primes, min_pi, max_pi, product = 1, mobius = 1):
    # print(f"{N=} {primes=} {product=} {mobius=}")
    for pi in range(min_pi, max_pi):
        p = primes[pi]
        if product * p > N:
            break
        yield -mobius, product * p
        yield from small_prime_factors(N, primes, pi + 1, max_pi, product * p, -mobius)

print(f_lim(1))