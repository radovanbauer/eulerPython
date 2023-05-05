import primesieve

def f(p, pow2):
    q = pow(2, pow(2, p, p - 1), p)
    return (-q) * pow(p, -1, pow2) % pow2
    # return 2**(2**p) // p % 2**p

def g(p, pow2):
    return f(p, pow2) % p

# print(f(3))
# print(g(31))

N = 10**7
sum = 0
pow2 = 2**1
primes = set(primesieve.primes(3, N))
for n in range(1, N):
    if n in primes:
        gg = g(n, pow2)
        sum += gg
        print(f"{n=} {gg=} {sum=}")
    pow2 *= 2
print(sum)