class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        @functools.lru_cache(None)
        def solve(r1, c1, r2, c2):
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -math.inf

            if r1 == n - 1 and c1 == n - 1:
                return grid[n - 1][n - 1]

            if r1 == r2 and c1 == c2:
                c = grid[r1][c1]
            else:
                c = grid[r1][c1] + grid[r2][c2]

            c += max(
                solve(r1 + 1, c1, r2 + 1, c2),
                solve(r1 + 1, c1, r2, c2 + 1),
                solve(r1, c1 + 1, r2, c2 + 1),
                solve(r1, c1 + 1, r2 + 1, c2)
            )

            return c

        return max(0, solve(0, 0, 0, 0))