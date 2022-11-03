from concurrent.futures import ProcessPoolExecutor
import sympy
import primesieve
from time import perf_counter


N = 10**7


def largest_prime_factor(n):
    return max(sympy.primefactors(n))


def calc_chunk(chunk):
    return sum(largest_prime_factor(4*k*k + 1) for k in chunk) % (10**18)


def modular_sqrt(a, p):

    def legendre_symbol(a, p):
        """ Compute the Legendre symbol a|p using
            Euler's criterion. p is a prime, a is
            relatively prime to p (if p divides
            a, then a|p = 0)
            Returns 1 if a has a square root modulo
            p, -1 otherwise.
        """
        ls = pow(a, (p - 1) // 2, p)
        return -1 if ls == p - 1 else ls

    """ Find a quadratic residue (mod p) of 'a'. p
        must be an odd prime.
        Solve the congruence of the form:
            x^2 = a (mod p)
        And returns x. Note that p - x is also a root.
        0 is returned is no square root exists for
        these a and p.
        The Tonelli-Shanks algorithm is used (except
        for some simple cases in which the solution
        is known from an identity). This algorithm
        runs in polynomial time (unless the
        generalized Riemann hypothesis is false).
    """
    # Simple cases
    #
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    # Partition p-1 to s * 2^e for an odd s (i.e.
    # reduce all the powers of 2 from p-1)
    #
    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1

    # Find some 'n' with a legendre symbol n|p = -1.
    # Shouldn't take long.
    #
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    # Here be dragons!
    # Read the paper "Square roots from 1; 24, 51,
    # 10 to Dan Shanks" by Ezra Brown for more
    # information
    #

    # x is a guess of the square root that gets better
    # with each iteration.
    # b is the "fudge factor" - by how much we're off
    # with the guess. The invariant x^2 = ab (mod p)
    # is maintained throughout the loop.
    # g is used for successive powers of n to update
    # both a and b
    # r is the exponent - decreases with each update
    #
    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m

if __name__ == '__main__':
    time1 = perf_counter()

    # workers = 8
    # ks = list(range(1, N + 1))
    # chunk_size = N//workers + 1
    # ks_chunks = [ks[k:k+chunk_size] for k in range(0, len(ks), chunk_size)]

    # with ProcessPoolExecutor(workers) as executor:
    #     print(sum(executor.map(calc_chunk, ks_chunks)) % (10**18))

    f = [4*k*k + 1 for k in range(0, N + 1)]
    maxp = (N + 1) * [1]
    primes = primesieve.primes(2*N)
    for p in primes:
        if p % 4 == 1:
            k1 = modular_sqrt(-pow(4, -1, p), p)
            k2 = p - k1
            for k in [k1, k2]:
                for i in range(k, N + 1, p):
                    assert f[i] % p == 0
                    maxp[i] = p
                    while f[i] % p == 0:
                        f[i] //= p
    for i in range(0, N + 1):
        if f[i] > 1:
            maxp[i] = f[i]
    print(sum(maxp[1:]) % (10**18))


    time2 = perf_counter()
    print(time2 - time1)
