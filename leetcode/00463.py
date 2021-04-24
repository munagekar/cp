class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        ans = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    continue

                if i + 1 >= r:
                    ans += 1
                elif grid[i + 1][j] == 0:
                    ans += 1

                if i - 1 < 0:
                    ans += 1
                elif grid[i - 1][j] == 0:
                    ans += 1

                if j + 1 >= c:
                    ans += 1
                elif grid[i][j + 1] == 0:
                    ans += 1

                if j - 1 < 0:
                    ans += 1
                elif grid[i][j - 1] == 0:
                    ans += 1

        return ans