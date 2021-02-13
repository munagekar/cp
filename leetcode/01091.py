class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        q = [(0, 0, 1)]
        l = len(grid)

        if grid[0][0]:
            return -1

        grid[0][0] = 1

        for (i, j, d) in q:
            if i == l - 1 and j == l - 1:
                return d
            for x in [i - 1, i, i + 1]:
                if x < 0 or x >= l:
                    continue
                for y in [j - 1, j, j + 1]:
                    if y < 0 or y >= l:
                        continue
                    if not grid[x][y]:
                        grid[x][y] = 1
                        q.append((x, y, d + 1))
        return -1