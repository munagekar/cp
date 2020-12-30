class Solution:
    def findLHS(self, nums: List[int]) -> int:

        m = collections.defaultdict(lambda: 0)

        for n in nums:
            m[n] = m[n] + 1

        ans = 0
        for k in list(m.keys()):
            if m[k + 1] != 0:
                ans = max(ans, m[k] + m[k + 1])
            if m[k - 1] != 0:
                ans = max(m[k] + m[k - 1], ans)

        return ans
