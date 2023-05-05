N = 10**8
MOD = 1008691207

cnt = -1

fact = 1
for k in range(0, N - 1):
    if k % 100000 == 0:
        print(k)
    fact = (fact * max(k, 1)) % MOD
    cnt = (cnt + fact * (N - 3 * k - 3)) % MOD

cnt = (cnt + fact * (N - 1) * N) % MOD

print(cnt)
