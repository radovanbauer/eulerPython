from concurrent.futures import ThreadPoolExecutor
from itertools import count
from math import floor, sqrt
import sympy
import primesieve
import random
import multiprocessing

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

        pis = list(range(0, len(primes)))
        random.shuffle(pis)
        workers = multiprocessing.cpu_count()
        chunkSize = len(pis) // workers + 1
        pis_chunks = [pis[i:i+chunkSize] for i in range(0, len(pis), chunkSize)]

        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(calc_chunk, N, primes, pis_chunk) for pis_chunk in pis_chunks]
            res = sum(future.result() for future in futures)

        res2 = res / N
        print(f"{N=} {res2=} {res2 - prev_res2} {workers=}")
        prev_res2 = res2
        N *= 2

def calc_chunk(N, primes, pis_chunk):
    return sum(calc_prime(N, primes, pi) for pi in pis_chunk)

def calc_prime(N, primes, pi):
    p = primes[pi]
    ppow = p * p
    sum_nom = 0
    while ppow <= N:
        sum_nom += N // ppow
        for mobius, factor in small_prime_factors(N // ppow, primes, 0, pi):
            sum_nom += mobius * N // (ppow * factor)
        ppow *= p
    return sum_nom / (p - 1)

def small_prime_factors(N, primes, min_pi, max_pi, product = 1, mobius = 1):
    # print(f"{N=} {primes=} {product=} {mobius=}")
    for pi in range(min_pi, max_pi):
        p = primes[pi]
        if product * p > N:
            break
        yield -mobius, product * p
        yield from small_prime_factors(N, primes, pi + 1, max_pi, product * p, -mobius)

if __name__ == "__main__":
    print(f_lim(1))