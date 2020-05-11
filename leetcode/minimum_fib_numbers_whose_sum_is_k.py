class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        a, b = 1, 1
        while b <= k:
            a, b = b, a + b

        ans = 0
        while k > 0:
            if a <= k:
                k -= a
                ans += 1
            b, a = a, b - a
        return ans