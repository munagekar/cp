class Solution:

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        def helper(nums):
            prev2 = nums[0]
            prev1 = max(nums[1], nums[0])

            for n in nums[2:]:
                tmp = prev1
                prev1 = max(n + prev2, prev1)
                prev2 = tmp

            return prev1

        s1 = helper(nums[:-1])
        s2 = helper(nums[1:])
        return max(s1, s2)