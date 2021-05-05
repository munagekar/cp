class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        ans = -1
        for k, v in c.items():
            if k == v:
                ans = max(ans, k)

        return ans