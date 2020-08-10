class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:

        mod = 10 ** 9 + 7

        max_pos = min(steps // 2 + 1, arrLen)

        dp = [0] * max_pos
        dp[0] = 1
        if max_pos >= 1:
            dp[1] = 1

        for i in range(2, steps + 1):
            new_arr = [0] * max_pos
            for j in range(0, max_pos):
                if j == 0:
                    new_arr[j] = dp[j] + dp[j + 1]
                elif j == max_pos - 1:
                    new_arr[j] = dp[j] + dp[j - 1]
                else:
                    new_arr[j] = dp[j] + dp[j + 1] + dp[j - 1]
                new_arr[j] %= mod
            dp = new_arr

        return dp[0]