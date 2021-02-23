class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not len(matrix) or not len(matrix[0]):
            return False

        r = 0
        c = len(matrix[0]) - 1

        while (r < len(matrix) and c >= 0):
            if target == matrix[r][c]:

                return True
            elif target > matrix[r][c]:
                r += 1
            else:
                c -= 1

        return False