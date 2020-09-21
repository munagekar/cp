from copy import deepcopy


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]

        sols = []

        def safe(row, col):
            for i in range(0, row):
                if board[i][col] == "Q":
                    return False

            for i in range(0, row):
                diff = row - i
                c1 = col - diff

                if c1 >= 0:
                    if board[i][c1] == "Q":
                        return False
                c2 = col + diff

                if c2 < n:
                    if board[i][c2] == "Q":
                        return False
            return True

        def solve(row):
            if row == n:
                sols.append(deepcopy(board))

            for col in range(n):
                if safe(row, col):
                    board[row][col] = "Q"
                    solve(row + 1)
                    board[row][col] = "."

        def f(board):
            return ["".join(row) for row in board]

        solve(0)

        return list(map(f, sols))
