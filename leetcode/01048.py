class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=len)

        dp = {}

        for w in words:
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))

        return max(dp.values())