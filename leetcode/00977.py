# Note: Both are O(n) due to timsort being used as the sorting algorithm

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        l, r = 0, len(A) - 1

        ans = []
        while l <= r:
            if abs(A[l]) >= abs(A[r]):
                ans.append(A[l] * A[l])
                l += 1
            else:
                ans.append(A[r] * A[r])
                r -= 1
        return ans[::-1]


class Solution2:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(i * i for i in A)
