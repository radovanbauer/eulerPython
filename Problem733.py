from time import perf_counter
from itertools import islice
time1 = perf_counter()

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, key, val):
        if self.root == None:
            self.root = Node(key, val)
        else:
            self.root.insert(key, val)

    def sum_for_max_key(self, maxkey):
        if self.root == None:
            return 0
        else:
            return self.root.sum_for_max_key(maxkey)

    def sum(self):
        if self.root == None:
            return 0
        else:
            return self.root.sum

    def depth(self):
        if self.root == None:
            return 0
        else:
            return self.root.depth()

    def __str__(self):
        if self.root == None:
            return "None"
        else:
            return str(self.root)

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val % MOD
        self.sum = self.val
        self.left = None
        self.right = None
        self.__depth = 1

    def insert(self, key, val):
        assert key != self.key
        if key < self.key:
            if self.left == None:
                self.left = Node(key, val)
            else:
                self.left.insert(key, val)
                self.__depth = max(self.__depth, self.left.depth() + 1)
        else:
            if self.right == None:
                self.right = Node(key, val)
            else:
                self.right.insert(key, val)
                self.__depth = max(self.__depth, self.right.depth() + 1)
        self.sum = (self.sum + val) % MOD

    def sum_for_max_key(self, maxkey):
        if maxkey == self.key:
            return self.val + (0 if self.left == None else self.left.sum)
        elif maxkey < self.key:
            return (0 if self.left == None else self.left.sum_for_max_key(maxkey))
        else:
            return self.val + (0 if self.left == None else self.left.sum) + (0 if self.right == None else self.right.sum_for_max_key(maxkey))
    
    def depth(self):
        return self.__depth

    def __str__(self):
        return f"{self.key}/{self.val}/{self.sum} ({None if self.left == None else str(self.left)}) ({None if self.right == None else str(self.right)})"

def S():
    s = 1
    while True:
        s = (s * 153) % 10000019
        yield s

N = 10**6
MOD = 1000000007

nums = list(islice(S(), N))
M = len(nums)

len1 = Tree()
len2 = Tree()
len3 = Tree()
len4 = Tree()
sum1 = Tree()
sum2 = Tree()
sum3 = Tree()
sum4 = Tree()
res = 0
for i, num in enumerate(nums):
    print(f"{i} {len1.depth()}")
    l3 = len3.sum_for_max_key(num)
    l2 = len2.sum_for_max_key(num)
    l1 = len1.sum_for_max_key(num)
    len4.insert(num, l3)
    len3.insert(num, l2)
    len2.insert(num, l1)
    len1.insert(num, 1)
    sum4.insert(num, sum3.sum_for_max_key(num) + l3 * num)
    sum3.insert(num, sum2.sum_for_max_key(num) + l2 * num)
    sum2.insert(num, sum1.sum_for_max_key(num) + l1 * num)
    sum1.insert(num, num)

print(sum4.sum())

time2 = perf_counter()
print(time2 - time1)