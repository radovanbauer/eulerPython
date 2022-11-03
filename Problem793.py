import itertools
from time import perf_counter
time1 = perf_counter()

def S():
    s = 290797
    while True:
        yield s
        s = s * s % 50515093


def count_leq(s, x):
    j = len(s) - 1
    res = 0
    for i in range(0, len(s)):
        while j > i and s[i] * s[j] > x:
            j -= 1
        if j > i:
            res += j - i
        else:
            break
    return res


N = 1000003
s = sorted(list(itertools.islice(S(), N)))
lo = 0
hi = 50515093**2
half = N * (N - 1) // 4
while hi - lo > 1:
    mid = (hi + lo) // 2
    cnt = count_leq(s, mid)
    if cnt <= half:
        lo = mid
    else:
        hi = mid
print(hi)

time2 = perf_counter()
print(time2 - time1)

