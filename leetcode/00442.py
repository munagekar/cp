class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = list()
        for x in nums:
            y = abs(x) - 1

            if nums[y] > 0:
                nums[y] *= -1

            else:
                res.append(abs(x))
        return res