class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        prefix = [0]
        running_sum = 0
        for x in A:
            running_sum += x
            prefix.append(running_sum)

        def avg(i, j):
            return (prefix[j] - prefix[i]) / (j - i)

        l = len(A)
        dp = [avg(i, l) for i in range(l)]

        for _ in range(K - 1):
            for i in range(0, l):
                for j in range(i + 1, l):
                    dp[i] = max(dp[i], avg(i, j) + dp[j])

        return dp[0]