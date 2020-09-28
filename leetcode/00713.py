class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        product = 1
        ans = 0

        if k <= 1:
            return 0

        for r, val in enumerate(nums):
            product *= val

            while product >= k:
                product /= nums[l]
                l += 1
            ans += r - l + 1

        return ans