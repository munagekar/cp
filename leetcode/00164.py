class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        maxi = max(nums)
        mini = min(nums)
        n = len(nums)

        buckets = {i: [] for i in range(0, n)}

        if n <= 2 or maxi == mini:
            return maxi - mini

        for x in nums:
            idx = (x - mini) * (n - 1) // (maxi - mini)
            buckets[idx].append(x)

        print(buckets)
        candidates = [(min(buckets[idx]), max(buckets[idx])) for idx in range(n) if buckets[idx]]

        ans = 0
        for c1, c2 in zip(candidates, candidates[1:]):
            ans = max(ans, c2[0] - c1[1])

        return ans