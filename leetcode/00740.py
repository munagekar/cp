class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = collections.defaultdict(lambda: 0)

        buckets = [0] * 10001

        for num in nums:
            buckets[num] += num

        for i in range(2, 10001):
            buckets[i] = max(buckets[i] + buckets[i - 2], buckets[i - 1])

        return buckets[10000]
