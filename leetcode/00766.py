def check(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    s_col = 1

    while s_col != cols:
        row = rows - 1
        element = matrix[row][s_col]
        col = s_col
        while col >= 0 and row >= 0:
            print(row, col)
            if element != matrix[row][col]:
                return False
            col -= 1
            row -= 1
        s_col += 1

    s_row = rows - 2

    while s_row >= 0:
        col = cols - 1
        element = matrix[s_row][col]
        row = s_row
        while row >= 0 and col >= 0:
            if element != matrix[row][col]:
                return False
            col -= 1
            row -= 1
        s_row -= 1

    return True


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return check(matrix)