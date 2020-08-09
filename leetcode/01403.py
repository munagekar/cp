class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        snums = sorted(nums, reverse=True)
        total = sum(nums)

        runner = 0

        res = []
        for n in snums:
            runner += n
            total -= n
            res.append(n)
            if runner > total:
                return res

