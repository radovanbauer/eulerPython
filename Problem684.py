def S(n):
    res = 0
    for b in range(0, 9):
        max_a = (n - b) // 9
        remainder_pow = (pow(10, max_a % 1000000006 + 1, 1000000007) - 1) * 111111112 % 1000000007
        sum = ((b + 1) * remainder_pow - max_a - 1) % 1000000007
        res += sum
    return res % 1000000007

fib = [0, 1]
for i in range(2, 91):
    fib.append(fib[i - 2] + fib[i - 1])

print(sum(map(S, fib[2:])) % 1000000007)