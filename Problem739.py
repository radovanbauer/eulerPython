from time import perf_counter
time1 = perf_counter()

N = 10**8
MOD = 1000000007

C = [0] * (N - 1)
C[0] = 1
C[1] = N - 2
x = N - 1
for n in range(2, N - 1):
    C[n] = C[n - 1] * pow(x - (n - 1), -1, MOD) * (x + (n - 1)) * (x - n) * pow(n, -1, MOD) % MOD

res = 0
L = [1, 3]
for n in range(2, N):
    L.append((L[-1] + L[-2]) % MOD)

for n in range(1, N):
    res = (res + L[n] * C[N - n - 1]) % MOD
print(res)

time2 = perf_counter()
print(time2 - time1)