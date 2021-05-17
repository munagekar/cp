class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        def explore(i, j):
            if i < 0 or i >= rows:
                return
            if j < 0 or j >= cols:
                return
            if board[i][j] != "O":
                return
            board[i][j] = "Y"
            explore(i + 1, j)
            explore(i - 1, j)
            explore(i, j + 1)
            explore(i, j - 1)

        for i in [0, rows - 1]:
            for j in range(cols):
                explore(i, j)

        for j in [0, cols - 1]:
            for i in range(rows):
                explore(i, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "Y":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

