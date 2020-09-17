class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        mask = 0
        ans = 0

        for i in range(32, -1, -1):
            mask = mask | 1 << i
            mask_nums = set([num & mask for num in nums])

            to_find = ans | 1 << i

            if any(num ^ to_find in mask_nums for num in mask_nums):
                ans = to_find

        return ans