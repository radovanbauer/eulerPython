from time import perf_counter
time1 = perf_counter()

MOD=1000000007
# K, N = 4, 20
K, N = 10 ** 8, 10 ** 16

fact = (K + 1) * [1]
for i in range(1, len(fact)):
    fact[i] = fact[i - 1] * i % MOD

factinv = (K + 1) * [1]
factinv[K] = pow(fact[K], -1, MOD)
for i in range(K - 1, -1, -1):
    factinv[i] = factinv[i + 1] * (i + 1) % MOD

def A(k, n):
    res = 0
    pow2 = pow(2, n // k * (k % 2), MOD)
    pow2_factor = pow(2, n // k * 2, MOD)
    for ones in range(k % 2, k + 1, 2):
        cnt = pow2 * factinv[ones] * factinv[(k - ones) // 2] * factinv[(k - ones) // 2]
        pow2 = pow2 * pow2_factor % MOD
        res += cnt
    return res * fact[k] % MOD

print(A(K, N))
time2 = perf_counter()
print(time2 - time1)