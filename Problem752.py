from sympy import factorint
from sympy import divisors
from time import perf_counter
time1 = perf_counter()

mod = 13

def mul(num1, num2, x):
    return ((num1[0] * num2[0] + 7 * num1[1] * num2[1]) % x, (num1[0] * num2[1] + num1[1] * num2[0]) % x)

def pow(num, n, x):
    if n == 1:
        return num
    p = pow(num, n // 2, x)
    if n % 2 == 1:
        return mul(num, mul(p, p, x), x)
    else:
        return mul(p, p, x)

def calc_good(x):
    xfact = factorint(x)
    res = 1
    for p, e in xfact.items():
        if p == 2 or p == 3:
            res *= 0
        if p % 7 == 0:
            res *= 42
        elif p % 28 in {1, 3, 9, 19, 25, 27}:
            res *= (p * p - 1 - (p - 1) * 2)
        else:
            res *= (p * p - 1)
        res *= p ** (2*e - 2)
    return res

def fast_gx(x):
    good = calc_good(x)
    if good == 0:
        return 0
    print(x)
    for div in divisors(good):
        if pow((1, 1), div, x) == (1, 0):
            return div
    assert False

print(sum(fast_gx(x) for x in range(2, 10**6 + 1)))

time2 = perf_counter()
print(time2 - time1)