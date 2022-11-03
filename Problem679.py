from functools import cache


keywords = ["FREE", "FARE", "AREA", "REEF"]
chars = "AEFR"


def generate(keywords, used=set(), res=[]):
    if (len(used) == len(keywords)):
        yield res.copy()
    else:
        for next in keywords:
            if next in used:
                continue
            used.add(next)

            res.append(next)
            yield from generate(keywords, used, res)
            res.pop()

            if len(res) > 0:
                for s in range(1, len(next)):
                    if res[-1].endswith(next[0:s]):
                        prev = res[-1]
                        res[-1] = res[-1] + next[s:]
                        yield from generate(keywords, used, res)
                        res[-1] = prev

            used.remove(next)


@cache
def fl3(n, last3, kws):
    if n == 3:
        if len(kws) == 0:
            return 1
        else:
            return 0
    res = 0
    for prev in chars:
        last4 = prev + last3
        if last4 in keywords:
            if last4 in kws:
                res += fl3(n - 1, last4[:3], kws - {last4})
        else:
            res += fl3(n - 1, last4[:3], kws)
    return res


def f(n):
    return sum(fl3(n, c1 + c2 + c3, frozenset(keywords)) for c1 in chars for c2 in chars for c3 in chars)


N = 30
print(f(N))
