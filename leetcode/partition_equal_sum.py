class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s // 2
        l = len(nums)

        # DP height = target+1, width l+1
        # DP sum, index
        dp = [[False] * (l + 1) for _ in range(target + 1)]

        # Init

        for i in range(0, l + 1):
            dp[0][i] = True

        for j in range(0, target + 1):
            dp[j][0] = False

        dp[0][0] = True

        for index in range(1, l + 1):
            for total in range(1, target + 1):
                dp[total][index] = dp[total][index - 1]
                if nums[index - 1] <= total:
                    dp[total][index] = dp[total][index - 1] or dp[total - nums[index - 1]][index - 1]

        return dp[target][l]