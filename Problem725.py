from functools import cache
from math import comb
from time import perf_counter
time1 = perf_counter()

MOD = 10 ** 16

def partitions(n, acc=[]):
    if n == 0:
        yield tuple(acc)
    for k in range(1, n + 1):
        acc.append(k)
        yield from partitions(n - k, acc)
        acc.pop()

def seq(d):
    for partition in partitions(d):
        if (len(partition) == 1):
            yield (d, d)
        else:
            for i in range(0, len(partition) + 1):
                yield partition[:i] + (d,) + partition[i:]

def s(n):
    res = 0
    for d in range(1, 10):
        for s in seq(d):
            if (len(s) <= n):
                res += s[0] * pow(10, n - 1, MOD) * comb(n - 1, len(s) - 1) % MOD
                res += ssum(n - 1, s[1:])
    return res % MOD

@cache
def ssum(n, seq):
    if len(seq) > n:
        raise Exception
    if (len(seq) == 0):
        return 0
    res = 0
    if (len(seq) < n):
        res += ssum(n - 1, seq)
    res += seq[0] * pow(10, n - 1, MOD) * comb(n - 1, len(seq) - 1) % MOD
    res += ssum(n - 1, seq[1:])
    return res % MOD

sum = 0
for n in range(1, 2022 + 1):
    sum += s(n)
    print(f"{n=}")
print(sum % MOD)

time2 = perf_counter()
print(time2 - time1)