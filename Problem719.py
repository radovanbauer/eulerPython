
import itertools
import concurrent.futures
import numpy

def is_s_number_sqrt(sqrt):
    return can_sum(str(sqrt ** 2), sqrt, 0)

def can_sum(ns, sum, depth):
    if (len(ns) == 0):
        return depth > 1 and sum == 0
    for l in range(1, len(ns) + 1):
        rest = sum - int(ns[:l])
        if (rest < 0):
            break
        if can_sum(ns[l:], rest, depth + 1):
            return True
    return False

def sum_chunk(chunk):
    return sum(sqrt ** 2 for sqrt in chunk if is_s_number_sqrt(sqrt))

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers = 12) as pool:
        sqrts = range(1, 10 ** 6 + 1)
        res = 0
        chunks = numpy.array_split(sqrts, 1000)
        print(sum(pool.map(sum_chunk, chunks)))
