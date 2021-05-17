class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        d = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        board = [[0] * n for _ in range(n)]

        board[row][column] = 1

        for _ in range(k):
            new_board = [[0] * n for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    if board[i][j] == 0:
                        continue
                    for x in d:
                        new_i = i + x[0]
                        new_j = j + x[1]
                        if new_i < 0 or new_i >= n:
                            continue
                        if new_j < 0 or new_j >= n:
                            continue
                        new_board[new_i][new_j] += board[i][j] / 8
            board = new_board

        return sum(sum(b) for b in board)

