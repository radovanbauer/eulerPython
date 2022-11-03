from itertools import count
from math import ceil, sqrt, floor
from time import perf_counter
time1 = perf_counter()

N = 10**16

def f(x, y):
    return x*x + x*y + 41*y*y

res = 0
for x in count(0):
    m = min(f(x, - (x//82)), f(x, - (x//82) - 1))
    if m > N:
        break
    y1 = (-x - sqrt(x*x - 4*41*(x*x - N))) / (82)
    y2 = (-x + sqrt(x*x - 4*41*(x*x - N))) / (82)
    # assert f(x, ceil(y1)) <= N and f(x, ceil(y1) - 1) > N, f"{x=}"
    # assert f(x, floor(y2)) <= N and f(x, floor(y2) + 1) > N, f"{x=}"
    if x == 0:
        res += floor(y2) - ceil(y1)
    else:
        res += (floor(y2) - ceil(y1) + 1) * 2
print(res)
    
time2 = perf_counter()
print(time2 - time1)