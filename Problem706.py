from time import perf_counter
time1 = perf_counter()

N = 10**5
MOD = 1000000007
cnt = [{}]
cnt[0][(1, 0, 0, 1)] = 3
cnt[0][(0, 1, 0, 0)] = 3
cnt[0][(0, 0, 1, 0)] = 3
for i in range(1, N):
    cnt.append({})
    for n in cnt[i - 1]:
        for d in range(0, 10):
            m = (0, 0, 0)
            if d % 3 == 0:
                m = ((n[0] + 1) % 3, n[1], n[2], (n[3] + n[0] + 1) % 3)
            elif d % 3 == 1:
                m = (n[2], (n[0] + 1) % 3, n[1], (n[3] + n[2]) % 3)
            elif d % 3 == 2:
                m = (n[1], n[2], (n[0] + 1) % 3, (n[3] + n[1]) % 3)
            cnt[i][m] = (cnt[i].get(m, 0) + cnt[i - 1][n]) % MOD
    # print(cnt[i])
res = sum(cnt[N - 1][n] for n in cnt[N - 1] if n[3] % 3 == 0) % MOD
print(res)

time2 = perf_counter()
print(time2 - time1)