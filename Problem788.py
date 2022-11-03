# D(1) = 9
# D(2) = 18
# D(3) = 18 + 9 + 9 * 2 * 9 + 9 * 9 = 270
# D(4) = 270 + 9 * (1 + 3 * 9) + 9 * 9 = 603

import math

N = 2022
MOD = 1000000007

fact = (N + 1) * [1]
for i in range(1, N + 1):
    fact[i] = fact[i - 1] * i % MOD

factinv = (N + 1) * [1]
factinv[N] = pow(fact[N], -1, MOD)
for i in range(N - 1, -1, -1):
    factinv[i] = factinv[i + 1] * (i + 1) % MOD

def comb(n, k):
    if k < 0 or k > n:
        return 0
    return fact[n] * factinv[k] * factinv[n - k] % MOD

D = (N + 1) * [0]
D[1] = 9
for i in range(2, N + 1):
    D[i] = (D[i - 1] + sum(comb(i, k) * pow(9, i - k + 1, MOD)
            for k in range(i // 2 + 1, i + 1))) % MOD
    print(f"{i=} {D[i]=}")
print(D[N])
