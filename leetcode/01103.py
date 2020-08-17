class Solution:
    def distributeCandies(self, candies: int, n: int) -> List[int]:
        res = [0] * n
        i = 0
        give = 1
        while candies > 0:
            res[i % n] += min(candies, give)
            candies -= give
            give += 1
            i += 1

        return res