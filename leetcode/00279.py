from math import sqrt

class Solution:
    def numSquares(self, n: int) -> int:

        # Perfect square
        m = int(sqrt(n))
        if m * m == n:
            return 1

        # Sum of 2

        for i in range(1, m + 1):
            j = n - i * i
            s = int(sqrt(j))
            if s * s == j:
                return 2

        # Sum of 4

        while n % 4 == 0:
            n /= 4

        if n % 8 == 7:
            return 4

        # Else 3
        return 3