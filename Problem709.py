from functools import cache
from math import comb
from re import X
import sys
from time import perf_counter
time1 = perf_counter()

N = 24680
MOD = 1020202009

fact = (N + 1) * [1]
for i in range(1, N + 1):
    fact[i] = fact[i - 1] * i % MOD

factinv = (N + 1) * [1]
factinv[N] = pow(fact[N], -1, MOD)
for i in range(N - 1, -1, -1):
    factinv[i] = factinv[i + 1] * (i + 1) % MOD

f_odd = (N + 1) * [0]
f_even = (N + 1) * [0]

f_odd[0] = 0
f_odd[1] = 1
f_even[0] = 1
f_even[1] = 0

for n in range(2, N + 1):
    f_odd[n] = sum(f_even[k] * f_even[n - k - 1]  *
                   factinv[k] * factinv[n - 1 - k] % MOD for k in range(0, n)) * fact[n - 1] % MOD
    f_even[n] = sum(f_even[k] * f_odd[n - k - 1] *
                    factinv[k] * factinv[n - 1 - k] % MOD for k in range(0, n)) * fact[n - 1] % MOD

print(f_even[N] + f_odd[N])

time2 = perf_counter()
print(time2 - time1)
