import itertools
from math import gcd
import more_itertools
from time import perf_counter
time1 = perf_counter()

def S():
    s = 290797
    while True:
        yield s
        s = s * s % 50515093

def T():
    return (s % 2000 - 1000 for s in S())

def line(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    if y1 == y2:
        a, b, c = 0, 1, -y1
        return a, b, c
    else:
        a = y1 - y2
        b = x2 - x1
        c = -(a * x1 + b * y1)
        return normalize(a, b, c)

def normalize(a, b, c):
    g = abs(gcd(a, b, c))
    if (a or b or c) < 0:
        g = -g
    return a / g, b / g, c / g

N = 2500
ts = list(itertools.islice(T(), 2*N + 1))
points = list({(ts[2 * k - 1], ts[2 * k]) for k in range(1, N + 1)})

lines = list({line(p1, p2) for p1 in points for p2 in points if p1 != p2})
get_ab = lambda x: (x[0], x[1])
lines.sort(key=get_ab)
lines_by_ab = itertools.groupby(lines, key=get_ab)
lines_ab_count = (more_itertools.ilen(line_group[1]) for line_group in lines_by_ab)

res = sum(cnt * (len(lines) - cnt) for cnt in lines_ab_count)
print(res)

time2 = perf_counter()
print(time2 - time1)