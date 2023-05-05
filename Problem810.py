from time import perf_counter
from bitarray import bitarray
time1 = perf_counter()

def xor_product(a, b):
    res = 0
    while b != 0:
        if b & 1 == 1:
            res ^= a
        b >>= 1
        a <<= 1
    return res

K = 5 * 10**6
N = 2**27

sieve = N * bitarray('0')

for a in range(2, N):
    if a < 10000 or a % 10000 == 0:
        print(a)
    for b in range(a, N):
        prod = xor_product(b, a)
        if prod >= N:
            break
        sieve[prod] = True

idx = 0
for n in range(2, N):
    if not sieve[n]:
        idx += 1
        if idx == K:
            print(n)

time2 = perf_counter()
print(time2 - time1)