def fact_pow2(n):
    res = 0
    pow2 = 2
    while pow2 <= n:
        res += n // pow2
        pow2 *= 2
    return res

def S2(n):
    if n == 0:
        return 0
    maxp2 = 1
    a = 0
    while maxp2 * 2 <= n:
        maxp2 *= 2
        a += 1
    m = n - maxp2 + 1
    return 2**a * (a - 3) + 3 + (m + 1) * a - fact_pow2(m)

print(S2(10**16))
