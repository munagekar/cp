# Maximum Size for Turbulent Subarray

class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        p = 0
        start = 0
        ans = min(1, len(A))
        n = len(A)

        while p + 1 != n:
            if p == start:
                p += 1
                if A[p] > A[start]:
                    ans = max(ans, 2)
                    sign = 1
                elif A[p] < A[start]:
                    ans = max(ans, 2)
                    sign = -1
                else:
                    start += 1
                continue
            if (sign == 1 and A[p + 1] < A[p]) or (sign == -1 and A[p + 1] > A[p]):
                p += 1
                sign *= -1
                ans = max(ans, p - start + 1)
            else:
                start = p

        return ans