from bisect import bisect_right
from functools import cache
from time import perf_counter
time1 = perf_counter()

MAX = 23416728348467685

fib = [1, 1]
while fib[-1] < MAX:
    fib.append(fib[-2] + fib[-1])

@cache
def G(N):
    if N == 0:
        return 0
    f = fib[bisect_right(fib, N) - 1]
    if N == f:
        return f + G(N - 1)
    else:
        return G(f) + G(N - f)

print(G(MAX))

time2 = perf_counter()
print(time2 - time1)