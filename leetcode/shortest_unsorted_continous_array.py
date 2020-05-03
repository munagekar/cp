class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        left = -1

        for i, (l1, l2) in enumerate(zip(sorted_nums, nums)):
            if l1 != l2:
                left = i
                break

        if left == -1:
            return 0

        right = len(nums) - 1

        while True:
            if sorted_nums[right] != nums[right]:
                break
            right -= 1

        return right - left + 1