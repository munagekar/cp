class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        minA = min(A)
        maxA = max(A)

        diff = maxA - minA

        ans = diff - 2 * K

        return max(0, ans)