from time import perf_counter
import sympy
time1 = perf_counter()

def next(n, k):
    if k < n // 2:
        return 2 * k
    else:
        return 2 * k - n + 1

def S(n):
    x = 1
    cnt = 1
    while next(n, x) != 1:
        x = next(n, x)
        cnt += 1
    return cnt

sum = 0
N = 60
divisors = sympy.ntheory.divisors(2**N - 1)
for d in divisors:
    s = S(d + 1)
    if s == N:
        sum += d + 1
print(sum)

time2 = perf_counter()
print(time2 - time1)