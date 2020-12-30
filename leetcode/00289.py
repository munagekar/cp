from copy import deepcopy


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        board2 = deepcopy(board)

        rows = len(board)
        cols = len(board[0])

        for x in range(rows):
            for y in range(cols):

                ln = 0
                dxs = [1, 1, 1, -1, -1, -1, 0, 0]
                dys = [1, -1, 0, 1, -1, 0, 1, -1]

                # Find Live Neighbors
                for dx, dy in zip(dxs, dys):
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < rows and 0 <= ny < cols:
                        if board2[nx][ny] == 1:
                            ln += 1

                # Rule 1  
                if ln < 2:
                    board[x][y] = 0

                # Rule 3
                if ln > 3:
                    board[x][y] = 0

                # Rule 4 and Rule 2
                if ln == 3:
                    board[x][y] = 1

        return board

    