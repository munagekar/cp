class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[0] = True

        wd = set(wordDict)
        for i in range(1, 1 + len(s)):
            for j in range(0, i):
                if dp[j] and s[j:i] in wd:
                    dp[i] = True
                    break

        return dp[-1]



