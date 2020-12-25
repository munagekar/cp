class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        pos = 0
        for i, n in enumerate(nums):
            if n == 0:
                continue
            nums[pos] = n
            pos += 1

        while pos < len(nums):
            nums[pos] = 0
            pos += 1

