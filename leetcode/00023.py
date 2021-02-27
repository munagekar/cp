class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1

        sign = 1
        if dividend < 0:
            sign *= -1

        if divisor < 0:
            sign *= -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        ans = 0

        while dividend >= divisor:
            temp = divisor
            count = 1
            while dividend > temp * 2:
                temp = temp * 2
                count *= 2

            dividend -= temp
            ans += count

        return sign * ans