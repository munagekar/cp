class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = 5
        a = 0
        while d <= n:
            a += n // d
            d *= 5

        return a