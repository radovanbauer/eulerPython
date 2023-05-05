from time import perf_counter
from math import comb
time1 = perf_counter()

def numberToBase(n, b):
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(str(n % b))
        n //= b
    return "".join(digits[::-1])

def numbers123():
    found = set([0, 1])
    yield 1
    n = 1
    while True:
        n += 1
        n123str = numberToBase(n, 4)
        n123 = int(n123str)
        cnt = 4 * [0]
        for c in n123str:
            cnt[int(c)] += 1
        if cnt[0] == 0 and cnt[1] in found and cnt[2] in found and cnt[3] in found:
            found.add(n123)
            yield n123

class Numbers123:
    def __init__(self):
        self.iter = numbers123()
        self.found = set([0])
        self.max = 0

    def is_number_123(self, n):
        while self.max < n:
            num = next(self.iter)
            self.found.add(num)
            self.max = num
        return n in self.found

numbers = Numbers123()

N = 111111111111222333
n = 0
while True:
    n += 1
    cnt = 0
    for cnt1 in range(0, n + 1):
        if not numbers.is_number_123(cnt1):
            continue
        for cnt2 in range(0, n + 1):
            if not numbers.is_number_123(cnt2):
                continue
            cnt3 = n - cnt1 - cnt2
            if not numbers.is_number_123(cnt3):
                continue
            cnt = cnt + comb(n, cnt1) * comb(n - cnt1, cnt2)
    if N - cnt <= 0:
        break
    N -= cnt
    # print(f"{n=} {cnt=} {N=}")

prefix = ""
digit_count = 4 * [0]
while len(prefix) < n:
    prefix += "0"
    for d in range(1, 4):
        cnt = 0
        prefix = prefix[:-1] + str(d)
        if d > 1:
            digit_count[d - 1] -= 1
        digit_count[d] += 1
        for cnt1 in range(0, n + 1):
            if not numbers.is_number_123(cnt1) or cnt1 < digit_count[1]:
                continue
            for cnt2 in range(0, n + 1):
                if not numbers.is_number_123(cnt2) or cnt2 < digit_count[2]:
                    continue
                cnt3 = n - cnt1 - cnt2
                if not numbers.is_number_123(cnt3) or cnt3 < digit_count[3]:
                    continue
                cnt = cnt + comb(n - len(prefix), cnt1 - digit_count[1]) * comb(n - len(prefix) - (cnt1 - digit_count[1]), cnt2 - digit_count[2])
        # print(f"{prefix=} {N=} {cnt=}")
        if N - cnt <= 0:
            break
        N -= cnt

print(int(prefix) % 123123123)

time2 = perf_counter()
print(time2 - time1)