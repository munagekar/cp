class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums) < s:
            return 0

        l = 0
        r = 1
        su = nums[0]
        ans = math.inf

        while r <= len(nums):

            if su < s or r == l:
                if r == len(nums):
                    break
                su += nums[r]
                r += 1

            elif su >= s:
                ans = min(ans, r - l)
                su -= nums[l]
                l += 1

        return ans
