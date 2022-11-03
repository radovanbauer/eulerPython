from time import perf_counter
time1 = perf_counter()

N = 10 ** 14
all = set()
for x in range(1, N + 1):
    # print(f"{x=}")
    if 2 * (x - 1) * (x - 2) > N:
        break
    for y in range(x - 2, 0, -2):
        a = (x * x - y * y) // 4
        b = a + y - 1
        if (a * b > N):
            break
        # c = a - (x - y) // 2
        # d = b + (x - y) // 2 + 1
        all.add(a * b)
        # print(f"{x=} {y=} {a}*{b} = {c}*{d} = {a*b} = {c*d}")
print(len(all))

time2 = perf_counter()
print(time2 - time1)