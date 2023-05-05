from functools import cache
from time import perf_counter
time1 = perf_counter()

# f(2*n + 1) = (2*n + 1) * (1 + f(n)/n)
# g(n) * n = f(n)
# g(1) = 1
# g(2*n) = g(n)
# g(2*n + 1) * (2*n + 1) = (2*n + 1) * (1 + g(n))
# g(2*n + 1) = 1 + g(n)
#
# S(n) = sum(g(n)**2 * n**2)
#
# sum(f(2k)**2 for k in range(k, 1, n + 1)) = 4*sum(f(k)**2 for n in range(k, 1, n + 1)) = 4*S(n)
# sum(f(2k + 1)**2 for k in range(1, n + 1)) = sum((2*k + 1)**2 * (1 + 2*f(k)/k + f(k)**2 / k**2) for k in range(1, n + 1))
#   = sum((2*k + 1)**2 + (2*k + 1)**2 * 2*f(k)/k + (2*k + 1)**2 * f(k)**2 / k**2) for k in range(1, n + 1))
# . = n * (11 + 12 * n + 4 * n**2) // 3 + 8 * sum(k * f(k)) + 8 * sum(f(k)) + 2 * sum(f(k) / k) + 4 * sum(f(k)**2) + 4 * sum(f(k) ** 2 / k) + sum(f(k)**2 / k**2)

def g(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return g(n // 2)
    else:
        return 1 + g(n // 2)

def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2 * f(n // 2)
    else:
        return n + f(n // 2) // (n // 2) * n


def S_orig(n):
    return sum(f(n)**2 for n in range(1, n + 1))

@cache
def Sf(m):
    res = 1
    if m > 1:
        res += 2 * Sf(m // 2)
    if m > 2:
        n = (m - 1) // 2
        res += n * (n + 2)
        res += 2 * Sf(n)#sum(f(k) for k in range(1, n + 1))
        res += Sg(n)#sum(f(k)//k for k in range(1, n + 1))
    return res

@cache
def Sf2(m):
    res = 1
    if m > 1:
        res += 4 * Sf2(m // 2)
    if m > 2:
        n = (m - 1) // 2
        res += n * (11 + 12 * n + 4 * n**2) // 3
        res += 8 * Skf(n)#sum(k * f(k) for k in range(1, n + 1))
        res += 8 * Sf(n)#sum(f(k) for k in range(1, n + 1))
        res += 2 * Sg(n)#sum(f(k) // k for k in range(1, n + 1))
        res += 4 * Sf2(n)
        res += 4 * Skg2(n)#sum(f(k) ** 2 // k for k in range(1, n + 1))
        res += Sg2(n)#sum(f(k)**2 // k**2 for k in range(1, n + 1))
    return res

@cache
def Skf(m):
    res = 1
    if m > 1:
        n = m // 2
        res += 4 * Skf(n) #sum(k * f(k) for k in range(1, n + 1))
    if m > 2:
        n = (m - 1) // 2
        res += n * (11 + 12 * n + 4 * n**2) // 3        
        res += 4 * Skf(n)#sum(k * f(k) for k in range(1, n + 1))
        res += 4 * Sf(n)#sum(f(k) for k in range(1, n + 1))
        res += Sg(n)#sum((f(k) // k) for k in range(1, n + 1))
    return res

@cache
def Sg(m):
    res = 1
    if m > 1:
        res += Sg(m // 2)
    if m > 2:
        n = (m - 1) // 2
        res += n#sum(1 for k in range(1, n + 1))
        res += Sg(n)#sum(g(k) for k in range(1, n + 1))
    return res

@cache
def Skg(m):
    res = 1
    if m > 1:
        res += 2 * Skg(m // 2)
    if m > 2:
        n = (m - 1) // 2
        res += n * (n + 2)
        res += 2*Skg(n)#sum((2*k) * (g(k)) for k in range(1, n + 1))
        res += Sg(n)#sum((1) * (g(k)) for k in range(1, n + 1))
    return res

@cache
def Sg2(m):
    res = 1
    if m > 1:
        res += Sg2(m // 2)
    if m > 2:
        n = (m - 1) // 2
        res += n
        res += 2*Sg(n)#sum(g(k) for k in range(1, n + 1))
        res += Sg2(n)#sum(g(k)**2 for k in range(1, n + 1))
    return res

@cache
def Skg2(m):
    res = 1
    if m > 1:
        n = m // 2
        res += 2 * Skg2(n)#sum(k * g(k)**2 for k in range(1, n + 1))
    if m > 2:
        n = (m - 1) // 2
        res += n * (n + 2) #sum((2*k + 1) for k in range(1, n + 1))
        res += 4 * Skg(n)#sum(k * g(k) for k in range(1, n + 1))
        res += 2 * Sg(n)#sum((1) * (2 * g(k)) for k in range(1, n + 1))
        res += 2 * Skg2(n)#sum((2*k) * g(k)**2 for k in range(1, n + 1))
        res += Sg2(n)#sum((1) * g(k)**2 for k in range(1, n + 1))
    return res

print(Sf2(10**16) % 1000000007)

time2 = perf_counter()
print(time2 - time1)
