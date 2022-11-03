from itertools import count


def digits(k, a, b):
    if a <= 0:
        a = 1
    if b <= a:
        return 0
    return pow(10, a - 1, 3**k) * 10**(b - a) // 3**k


N = 10**16
res = 0
for k in count(1):
    x = digits(k, N - 3**k, N + 10 - 3**k)
    if x == 0:
        break
    print(f"{k=} {x=}")
    res += x
res = res % 10**10 + res // 10**10
print(res)
