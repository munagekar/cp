class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        maxi = len(nums) + 10
        # Remove all negatives
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = maxi

        for i in range(len(nums)):
            index = nums[i]
            index = abs(index)
            if l <= index - 1 or index <= 0:
                continue

            nums[index - 1] = min(-nums[index - 1], nums[index - 1])

        for i, n in enumerate(nums):
            if n > 0:
                return i + 1

        return len(nums) + 1