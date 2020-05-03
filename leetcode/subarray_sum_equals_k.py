class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        s = 0
        ans = 0
        for num in nums:
            s += num
            ans = ans + d.get(s - k, 0)
            d[s] = 1 + d.get(s, 0)

        return ans