def is_duodigit(n):
    digits = set()
    while n > 0:
        digits.add(n % 10)
        n //= 10
    return len(digits) <= 2

def d(n, suffixes = [0], suffix_len = 0):
    while True:
        new_suffixes = []
        for digit in range(0, 10):
            for suffix in suffixes:
                s = digit * 10 ** suffix_len + suffix
                multiple = n * s
                if multiple != 0 and is_duodigit(multiple):
                    return multiple
                if is_duodigit(multiple % (10 ** (suffix_len + 1))):
                    new_suffixes.append(s)
        suffixes = new_suffixes
        suffix_len += 1
        print(f"{len(suffixes)} {suffix_len}")

def D(k):
    sum = 0
    for k in range(1, k + 1):
        sum += d(k)
        print(k)
    return sum

print(f"{D(50000):.12e}")
