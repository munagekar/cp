import itertools
import operator


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        k = abs(k)
        r = 0

        m = {}
        m[0] = -1
        for i, x in enumerate(nums):
            r += x
            if k != 0:
                r %= k

            prev = m.get(r)

            if prev != None:
                print(prev, i)
                if i - prev > 1:
                    return True
            else:
                m[r] = i

        return False