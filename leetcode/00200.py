class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        r = len(grid)
        c = len(grid[0])

        def dfs(i, j):

            if i < 0 or i >= r:
                return
            if j < 0 or j >= c:
                return
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        counter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != '0':
                    dfs(i, j)
                    counter += 1

        return counter