N = 1234567890123456789
Nstr = str(N)
M = len(Nstr)

cnt = [{} for i in range(M)]
dsum = [{} for i in range(M)]
cnt[0][0] = 1
dsum[0][0] = 0
for i in range(0, M - 1):
    for s in cnt[i]:
        for d in range(0, 10):
            cnt[i + 1][s + d] = cnt[i + 1].get(s + d, 0) + cnt[i][s]
            dsum[i + 1][s + d] = dsum[i + 1].get(s + d, 0) + (dsum[i][s] * 10 + d * cnt[i][s])
# print(cnt)
# print(dsum)

res = {sum(int(c) for c in Nstr) : N}
for i in range(M):
    for d in range(0, int(Nstr[i])):
        for s in cnt[M - i - 1]:
            dd = s + d + sum(int(c) for c in Nstr[:i])
            res[dd] = res.get(dd, 0) + dsum[M - i - 1][s] + int(Nstr[:i] + str(d) + (M - i - 1) * '0') * cnt[M - i - 1][s]
F = sum(s / d for d, s in res.items() if d != 0)
print(f"{F:-.12e}")