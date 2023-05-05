from itertools import count
from math import sqrt
from time import perf_counter
time1 = perf_counter()

W = 10000
H = 10000
MOD = 1000000007

fib = [1, 1]
while fib[-1] < W + H:
    fib.append(fib[-2] + fib[-1])
fibset = set(fib)

moves = []
for x in range(0, W + 1):
    for y in range(0, H + 1):
        s = sqrt(x * x + y * y)
        if s in fibset and s * s == x * x + y * y:
            moves.append((x, y))

F = [(H + 1) * [0] for i in range(0, W + 1)]
F[0][0] = 1

for w in range(0, W + 1):
    for h in range(0, H + 1):
        if w != 0 or h != 0:                
            for move in moves:
                if w >= move[0] and h >= move[1]:
                    F[w][h] = (F[w][h] + F[w - move[0]][h - move[1]]) % MOD

print(F[W][H])

time2 = perf_counter()
print(time2 - time1)