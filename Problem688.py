from math import floor, sqrt

def Sk(N, k):
    min_n = k*(k - 1) // 2
    if min_n > N:
        return 0
    x = (N - min_n + 1) // k
    res = x*(x - 1)//2*k + x*((N - min_n + 1) % k)
    return res

N = 10**16
K = floor(sqrt(2*N))
while K*(K + 1)//2 <= N:
    K += 1
assert K*(K - 1)//2 < N
assert K*(K + 1)//2 > N
print(sum(Sk(N, k) for k in range(1, K + 1)) % 1000000007)