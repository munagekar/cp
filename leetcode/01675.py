class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        nums = [-(n + (n & 1) * n) for n in nums]
        m = - max(nums)
        heapq.heapify(nums)
        res = math.inf

        while True:
            a = - heapq.heappop(nums)
            res = min(res, a - m)

            if a % 2 == 1:
                return res

            heapq.heappush(nums, -a // 2)
            m = min(m, a // 2)