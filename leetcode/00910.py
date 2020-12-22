class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()

        ans = A[-1] - A[0]

        for i in range(0, len(A) - 1):
            maxi = max(A[-1], A[i] + 2 * K)
            mini = min(A[i + 1], A[0] + 2 * K)
            ans = min(maxi - mini, ans)

        return ans
