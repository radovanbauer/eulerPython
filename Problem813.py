from bitarray import bitarray

def iter(n):
    return n ^ (n << 1) ^ (n << 3)

n = 1
nums = [1]
for i in range(1, 33):
    n = iter(n)
    nums.append(n)
    print("   " * (33 - i) + f"{n:b}")

# for i in range(1, 6):
#     print(f"{i=} {nums[2**i]=:b}")
#     assert nums[2**i] == 1 + 2**(2**i) + 2**(3 * 2**i)
#     for k in range(2**i, 2**(i + 1)):
#         if 2 ** i + k < len(nums):
#             assert nums[2**i + k] == nums[k] ^ (nums[k] << (2 ** i)) ^ (nums[k] << (3 * 2 ** i))

M = 10**9 + 7

def calc(n):
    if n == 0:
        arr = bitarray(M - 1)
        arr.setall(0)
        arr[0] = 1
        return arr
    i = n.bit_length()
    assert 2 ** (i - 1) <= n and 2 ** i > n
    k = n - 2 ** (i - 1)
    p = calc(k)
    # res = p.copy()
    # shift1 = 2**i
    # shift2 = 3 * 2**i
    # for j in range(0, M - 1):
    #     res[(j + shift1) % (M - 1)] ^= p[j]
    #     res[(j + shift2) % (M - 1)] ^= p[j]
    shift1 = bitarray(2 * M - 2)
    shift1.setall(0)
    shift1[:M - 1] ^= p
    shift1 >>= (2**i) % (M - 1)
    shift2 = bitarray(2 * M - 2)
    shift2.setall(0)
    shift2[:M - 1] ^= p
    shift2 >>= (3 * 2**i) % (M - 1)
    res = p.copy()
    res ^= shift1[:M - 1]
    shift1 <<= M - 1
    res ^= shift1[:M - 1]
    res ^= shift2[:M - 1]
    shift2 <<= M - 1
    res ^= shift2[:M - 1]

    print(f"{n=} {res[:1000]}")
    return res

calc(16)

# P(2**n) = 1 + 2**(2**n) + 2**(3 * 2**n)
# P(2**n + k) = P(k) ^ (P(k) << (2**n)) ^ (P(k) << (3 * 2 ** n))