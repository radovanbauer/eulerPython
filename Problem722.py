from time import perf_counter
from itertools import count
from decimal import Decimal
time1 = perf_counter()

# d**k * sum(q**(n*d) for n in range(1, ...))
# d**k * q**d / (1 - q**d)
# d**k * (2**l - 1)**d / ((2**l)**d - (2**l - 1)**d)

q = Decimal(1) - Decimal(2) ** (-25)
k = 15

res = 0
for d in count(1):
    res += d**k * q**d / (1 - q**d)
    if d % 1000000 == 0:
        print(f"{d=} {res=}")


time2 = perf_counter()
print(time2 - time1)