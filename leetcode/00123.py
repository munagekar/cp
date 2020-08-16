class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        # Build left

        arr_left = [0]
        min_left = prices[0]

        for p in prices[1:]:
            arr_left.append(max(arr_left[-1], p - min_left))
            min_left = min(p, min_left)

        max_right = prices[-1]
        arr_right = [0] * len(prices)
        for i in range(len(prices) - 2, -1, -1):
            arr_right[i] = max(arr_right[i + 1], max_right - prices[i])
            max_right = max(prices[i], max_right)

        ans = 0
        for i, j in zip(arr_left, arr_right):
            ans = max(ans, i + j)

        return ans