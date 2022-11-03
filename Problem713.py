def T(n, m):
    if m > n // 2:
        return n - m + 1
    small = n // (m - 1)
    large = small + 1
    return n % (m - 1) * large * (large - 1) // 2 + (m - 1 - n % (m - 1)) * small * (small - 1) // 2

N = 10**7
res = sum(T(N, m) for m in range(2, N + 1))
print(res)
