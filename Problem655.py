
# print(len(str(10**31 // X)))
# print(10**31 // X)
# print((10**32 - 1) // X)

# k * X = P1 * 10 ** 16 + P2
# (k1 * 10**16 + k2) * X = P1 * 10 ** 16 + P2
# k2 * X % 10**16 = P2
# k1 * X + k2 * X // 10**16 = P1
# k1 * X == P1 - k2 * X // 10**16

def reverse(n):
    return int(str(n)[::-1])


# for n in range(len(str(X)), N + 1):
#     m = (n + 1) // 2
#     for k2 in range(0, 10**m):
#         P2 = k2 * X % 10**m
#         if P2 % 10 == 0 or len(str(P2)) < m:
#             continue
#         if n % 2 == 0:
#             P1 = reverse(P2)
#             z = P1 - k2 * X // 10**m
#             if z % X == 0:
#                 print(f"{n=} {m=} {k2=} {z=} {P1=} {P2=} {P1 * 10**m + P2=}")
#                 assert (P1 * 10**m + P2) % X == 0
#         if n % 2 == 1:
#             P1 = reverse(P2) // 10
#             z = P1 - k2 * X // 10**m
#             if z % X == 0:
#                 print(f"{n=} {m=} {k2=} {z=} {P1=} {P2=} {P1 * 10**m + P2=}")
#                 assert (P1 * 10**m + P2) % X == 0

# X = 109
# N = 5
X = 10000019
N = 32
res = 0
for n in range(len(str(X)), N + 1):
    cnt = {0: 1}
    for i in range(0, (n + 1) // 2):
        coef = 10**i + 10**(n - i - 1) if i < n - i - 1 else 10**i
        new_cnt = {}
        for key, val in cnt.items():
            for d in range(0, 10):
                if i == 0 and d == 0:
                    continue
                new_cnt[(key + coef * d) % X] = new_cnt.get((key + coef * d) % X, 0) + val
        cnt = new_cnt
    print(f"{n=} {cnt.get(0, 0)}")
    res += cnt.get(0, 0)
print(res)