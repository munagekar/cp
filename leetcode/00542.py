class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])

        ans = [[-1] * col for _ in range(row)]

        queue = collections.deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    queue.append((i, j))

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while queue:
            i, j = queue.popleft()

            for (di, dj) in dirs:
                ni = i + di
                nj = j + dj

                if 0 <= ni < row and 0 <= nj < col and ans[ni][nj] == -1:
                    ans[ni][nj] = ans[i][j] + 1
                    queue.append((ni, nj))

        return ans