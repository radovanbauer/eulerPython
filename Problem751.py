from math import floor, pow

def calc(b):
    res = "2."
    while (len(res) < 26):
        b = floor(b) * (b - floor(b) + 1)
        a = floor(b)
        res += str(a)
    return res[:26]

def longest_prefix(s1, s2):
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            return s1[:i]
    return s1

min = 2.22
max = 2.23
res = "2.22"
while (len(res) < 26):
    min_res = calc(min)
    max_res = calc(max)
    res = longest_prefix(min_res, max_res)
    min = float(res)
    max = min + pow(10, -len(res) + 2)

print(res)
