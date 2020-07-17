import operator
from itertools import accumulate


class Solution:
    def maxSumTwoNoOverlap(self, a: List[int], f: int, s: int) -> int:

        a = list(accumulate(a, operator.add))
        print(a)
        res, fm, sm = a[f + s - 1], a[f - 1], a[s - 1]

        for i in range(f + s, len(a)):
            fm = max(fm, a[i - s] - a[i - f - s])
            res = max(res, fm + a[i] - a[i - s])

        for i in range(f + s, len(a)):
            sm = max(sm, a[i - f] - a[i - s - f])
            res = max(res, sm + a[i] - a[i - f])

        return res