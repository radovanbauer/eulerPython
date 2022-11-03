from math import floor, log

def kpower(n, k):
    return sum(int(c)**k for c in str(n))

MAXD = 16
MAX = 10**MAXD
MAXPOW = floor(log(MAX, 2))

res = 0
for pow in range(1, MAXPOW + 1):
    nums = {0}
    for d in range(1, MAXD + 1):
        newnums = set()
        for k in range(0, 10):
            for n in nums:
                if n < MAX:
                    newnums.add(k**pow + n)
        nums = newnums
        for n in nums:
            if (len(str(n + 1)) == d and kpower(n + 1, pow) == n):
                res += n + 1
            if (n > 1 and len(str(n - 1)) == d and kpower(n - 1, pow) == n):
                res += n - 1
print(res)