class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        l1 = len(nums1)
        l2 = len(nums2)

        dp = [[-math.inf] * (l2 + 1) for _ in range(l1 + 1)]

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                p = nums1[i - 1] * nums2[j - 1]
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + p, p)

        return dp[-1][-1]