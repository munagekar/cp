class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1
        memo = {}
        x = math.ceil(n / 25)

        def s(a, b):

            if (a, b) in memo:
                return memo[(a, b)]

            if a <= 0 and b <= 0:
                return 0.5

            if a <= 0:
                return 1

            if b <= 0:
                return 0

            memo[(a, b)] = 0.25 * (s(a - 4, b) + s(a - 3, b - 1) + s(a - 2, b - 2) + s(a - 1, b - 3))
            return memo[(a, b)]

        return s(x, x)


