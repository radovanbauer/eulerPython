from functools import reduce
import primesieve

MOD = 1000000007
N = 10**8


def max_pow(a, b):
    max = 1
    while max * a <= b:
        max *= a
    return max


def lcm_fact(n, mod):
    return reduce(lambda a, b: a * b % MOD, (max_pow(p, n) for p in primesieve.primes(n + 1)), 1)


def f(n):
    return lcm_fact(n, MOD)*2 % MOD


print(f(N))
