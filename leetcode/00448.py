class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for n in nums:
            n = abs(n)
            if nums[n - 1] > 0:
                nums[n - 1] *= -1

        ans = [i + 1 for i, n in enumerate(nums) if n > 0]
        return ans