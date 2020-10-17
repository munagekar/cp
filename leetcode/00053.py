class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        runner = nums[0]
        for n in itertools.islice(nums, 1, len(nums)):
            runner = max(n, runner + n)
            ans = max(ans, runner)

        return ans