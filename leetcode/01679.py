class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)

        ans = 0
        for i in c:
            if c[k - i] > 0:
                ans += min(c[i], c[k - i])
        return ans // 2 