# 2 ** k = p * 10 ** (floor(log(2**k,10))-3) + q
# p = floor((2 ** k) / (10 ** (floor(log(2**k,10))-3)))
# p = floor(10 ** (k * log(2, 10) - floor(log(2**k,10)) + 3))

from math import floor, log

l2 = log(2, 10)
idx = 0
k = 0
while idx < 678910:
    k += 1
    res = floor(10 ** (k * l2 - floor(k * l2) + 2))
    if res == 123:
        idx += 1
        print(f"{idx}: {k}")
