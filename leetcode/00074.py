class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        low = 0

        cols = len(matrix[0])
        high = len(matrix) * len(matrix[0]) - 1

        while low <= high:

            mid = (low + high) // 2
            r, c = divmod(mid, cols)

            val = matrix[r][c]

            if val == target:
                return True

            if val > target:
                high = mid - 1

            else:
                low = mid + 1

        return False