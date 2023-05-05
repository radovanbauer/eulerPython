from concurrent.futures import ThreadPoolExecutor
from itertools import count
from math import floor, isqrt
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
    # while N < 10**20:
    primes = primesieve.primes(1000)
    # primes = [2, 3, 5, 7]
    res = 0

    pis = list(range(0, len(primes)))
    # random.shuffle(pis)
    workers = multiprocessing.cpu_count()
    chunkSize = len(pis) // workers + 1
    pis_chunks = [pis[i:i+chunkSize] for i in range(0, len(pis), chunkSize)]

    res = 0
    for p in range(0, len(primes)):
        p_res, cnt = iterate_prime(primes, p)
        res += p_res
        print(f"{primes[p]=} {p_res=} {cnt=} {res=}")

    # with ThreadPoolExecutor(max_workers=1) as executor:
    #     futures = [executor.submit(calc_chunk, N, primes, pis_chunk) for pis_chunk in pis_chunks]
    #     res = sum(future.result() for future in futures)

    print(f"{N=} {res2=} {res2 - prev_res2} {workers=}")
    prev_res2 = res2

def calc_chunk(N, primes, pis_chunk):
    return sum(calc_prime(N, primes, pi) for pi in pis_chunk)

def iterate_prime(primes, pi):
    delta = 1
    N = primes[pi] ** 2
    res = calc_prime(N, primes, pi)
    cnt = 0
    while abs(delta) > 10**(-15):
        N = N * 2
        new = calc_prime(N, primes, pi)
        delta = new - res
        res = new
        cnt += 1
        # print(f"{primes[pi]=} {N=} {res=} {delta=}")
    return res, cnt

def calc_prime(N, primes, pi):
    p = primes[pi]
    ppow = p * p
    sum_nom = 0
    cnt = 0
    while ppow <= N:
        sum_nom += N // ppow
        for mobius, factor in small_prime_factors(N // ppow, primes, 0, pi):
            sum_nom += mobius * (N // (ppow * factor))
            cnt += 1
        ppow *= p
    # print(f"{p=} {sum_nom / p / N=}")
    return sum_nom / (p * N)

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