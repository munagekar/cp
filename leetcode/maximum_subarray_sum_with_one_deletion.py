class Solution:
    def maximumSum(self, arr: List[int]) -> int:

        maxarr = max(arr)
        if maxarr < 0:
            return maxarr

        ignored = 0
        res = 0
        not_ignored = 0
        for num in arr:
            if num >= 0:
                ignored += num
                not_ignored += num

            else:
                ignored = max(not_ignored, ignored + num)
                not_ignored += num
            ignored = max(ignored, 0)
            not_ignored = max(not_ignored, 0)
            res = max(res, ignored, not_ignored)

        return res