class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:

        size = [0] * (len(arr) + 2)

        if m == len(arr):
            return m

        res = -1
        for step, i in enumerate(arr, 1):
            l = size[i - 1]
            r = size[i + 1]

            s = l + r + 1

            if l == m or r == m:
                res = step - 1

            size[i - l] = size[i + r] = s

        return res