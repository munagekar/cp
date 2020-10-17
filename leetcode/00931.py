from copy import deepcopy


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        minsum = deepcopy(A[-1])

        l = len(A)

        for row in range(l - 2, -1, -1):
            temp = []
            for i in range(l):
                mini = minsum[i]
                if i > 0:
                    mini = min(minsum[i - 1], mini)
                if l > i + 1:
                    mini = min(minsum[i + 1], mini)
                temp.append(A[row][i] + mini)
            minsum = temp
        return min(minsum)