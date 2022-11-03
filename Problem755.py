from functools import cache
from time import perf_counter
time1 = perf_counter()

MAX = 10 ** 13

fib = [1, 2]
fibsum = [1, 3]
while fib[-1] < MAX:
    fib.append(fib[-2] + fib[-1])
    fibsum.append(fibsum[-1] + fib[-1])

@cache
def S(n, maxfi):
    if maxfi < 0:
        return 0  
    if n == 0:
        return 1
    if n == 1:
        return 2
    while maxfi >= 0 and fib[maxfi] > n:
        maxfi = maxfi - 1
    if maxfi == 0:
        return 2
    if fibsum[maxfi] < n:
        return S(fibsum[maxfi], maxfi)

    F = fib[maxfi]
    return S(n - F, maxfi - 1) + S(n, maxfi - 1) - S(F - 1, maxfi - 1) + S(F - 1, maxfi)

print(S(10**13, len(fib) - 1))

time2 = perf_counter()
print(time2 - time1)