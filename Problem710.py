from functools import cache
from itertools import count

MOD = 1000000

@cache
def t_odd(n):
    res = 0
    match n:
        case 0 | 1:
            res = 0
        case 2:
            res = 1
        case 3:
            res = 0
        case 4:
            res = 1
        case _ if n % 2 == 0:
            k = n // 2
            res = t_odd(2*(k - 1)) + pow(2, k - 3, MOD) + t_even(2*(k - 2))
        case _:
            k = n // 2
            res = t_odd(2*(k - 1) + 1) + t_even(2*k)
    return res % MOD

@cache
def t_even(n):
    res = 0
    match n:
        case 0 | 1 | 2 | 3:
            res = 0
        case 4:
            res = 1
        case 6:
            res = 2
        case _ if n % 2 == 0:
            k = n // 2
            res = pow(2, k - 4, MOD) + 2*t_even(2*(k - 1)) - t_even(2*(k - 2)) + t_even(2*(k - 3))
        case _:
            res = 0
    return res % MOD

def t(n):
    return (t_odd(n) + t_even(n)) % MOD

print(next(n for n in count(42) if t(n) == 0))