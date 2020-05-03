from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        res = []
        for i in range(k):
            # print(i)
            # print(nums[i])
            while len(d) > 0 and nums[d[-1]] < nums[i]:
                d.pop()
            d.append(i)
            # print(d)
        res.append(nums[d[0]])

        for i in range(k, len(nums)):
            if d[0] < i - k + 1:
                d.popleft()

            while len(d) > 0 and nums[d[-1]] < nums[i]:
                d.pop()
            d.append(i)
            res.append(nums[d[0]])

        return res