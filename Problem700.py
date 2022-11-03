coins = [1504170715041707]
idx = [1]


for n in range(2, 100000000):
    x = 1504170715041707 * n % 4503599627370517
    if x < coins[len(coins) - 1]:
        print(coins)
        coins.append(x)
        idx.append(n)

for x in range(coins[len(coins) - 1] - 1, 0, -1):
    i = x * 3451657199285664 % 4503599627370517
    while i < idx[len(idx) - 1]:
        idx.pop()
        coins.pop()
    coins.append(x)
    idx.append(i)
    if (x % 1000 == 0):
        print(x)

print(sum(coins))