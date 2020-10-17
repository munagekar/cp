class Solution:
    def countOdds(self, low: int, high: int) -> int:
        he = (high + 1) // 2
        le = (low) // 2

        return he - le
