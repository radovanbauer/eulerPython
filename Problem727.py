# sqrt((ex - ax)**2 + (ey - ay)**2) = ra + e
# sqrt((ex - bx)**2 + (ey - by)**2) = rb + e
# sqrt((ex - cx)**2 + (ey - cy)**2) = rc + e

from sympy import Point, Triangle, Circle
from math import sqrt, gcd

def d(ra, rb, rc):
    a = rb + rc
    b = ra + rc
    c = ra + rb
    A = Point(0, 0, evaluate=False)
    B = Point(c, 0, evaluate=False)
    s = (a + b + c) / 2
    S = sqrt(s * (s - a) * (s - b) * (s - c))
    Cy = 2 * S / c
    Cx = sqrt(b*b - Cy*Cy)
    C = Point(Cx, Cy, evaluate=False)
    t = Triangle(A, B, C, evaluate=False)
    D = t.incenter

    lo = 0
    hi = rc
    error = 1e-14
    E = None
    while hi - lo > error:
        e = (lo + hi) / 2
        bb = rb + e
        aa = ra + e
        ss = (c + bb + aa) / 2
        SS = sqrt(ss * (ss - aa) * (ss - bb) * (ss - c))
        Ey = 2 * SS / c
        Ex = sqrt(bb * bb - Ey*Ey)
        E = Point(Ex, Ey, evaluate=False)
        EC = E.distance(C)
        # print(f"{e=} {EC=} {rc + e=}")
        if EC > rc + e:
            lo = e
        else:
            hi = e
    
    return D.distance(E)



sum = 0
cnt = 0
for ra in range(1, 101):
    for rb in range(ra + 1, 101):
        print(f"{ra} {rb}")
        for rc in range(rb + 1, 101):
            if gcd(ra, rb, rc) == 1:
                sum += d(ra, rb, rc)
                cnt += 1
print(sum / cnt)