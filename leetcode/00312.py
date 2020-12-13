class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [n for n in nums if n != 0] + [1]

        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for k in range(3, n + 1):
            for l in range(0, n - k + 1):
                r = l + k - 1
                for i in range(l + 1, r):
                    dp[l][r] = max(dp[l][r], dp[l][i] + dp[i][r] + nums[l] * nums[i] * nums[r])

        return dp[0][n - 1]