class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l = len(nums)

        def helper(low, high):
            if low == high:
                return low

            mid = (low + high) // 2

            if mid > 0 and nums[mid] < nums[mid - 1]:
                return helper(low, mid - 1)

            elif mid < l and nums[mid] < nums[mid + 1]:
                return helper(mid + 1, high)
            return mid

        return helper(0, len(nums) - 1)


class Solution2:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i

        return len(nums) - 1