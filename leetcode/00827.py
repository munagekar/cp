class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        m = {0: 0}
        n = len(grid)

        def dfs(x, y, index):
            if not 0 <= x < n:
                return 0
            if not 0 <= y < n:
                return 0

            if grid[x][y] != 1:
                return 0

            grid[x][y] = index

            count = 1
            for a, b in ((x + 1, y), (x, y + 1), (x, y - 1), (x - 1, y)):
                count += dfs(a, b, index)

            return count

        index = 2

        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    m[index] = dfs(x, y, index)
                    index += 1

        ans = max(m.values())

        for x in range(n):
            for y in range(n):
                if grid[x][y] != 0:
                    continue

                c = 0
                seen = set()
                for a, b in ((x + 1, y), (x, y + 1), (x, y - 1), (x - 1, y)):
                    if not 0 <= a < n or not 0 <= b < n:
                        continue
                    idx = grid[a][b]
                    if idx not in seen:
                        c += m[grid[a][b]]
                        seen.add(idx)
                ans = max(ans, c + 1)

        return ans