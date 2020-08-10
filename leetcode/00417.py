def dfs(x, y, grid, r, c, heights):
    if grid[y][x] == True:
        return

    grid[y][x] = True

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in directions:
        newx, newy = x + dx, y + dy
        if newy >= 0 and newy < r and newx >= 0 and newx < c and heights[newy][newx] >= heights[y][x] and not \
        grid[newy][newx]:
            dfs(newx, newy, grid, r, c, heights)


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        r = len(matrix)
        c = len(matrix[0])
        p = [[False] * c for _ in range(r)]
        a = [[False] * c for _ in range(r)]

        for x in range(c):
            dfs(x, 0, p, r, c, matrix)
            dfs(x, r - 1, a, r, c, matrix)

        for y in range(r):
            dfs(0, y, p, r, c, matrix)
            dfs(c - 1, y, a, r, c, matrix)

        res = []
        for x in range(c):
            for y in range(r):
                if p[y][x] and a[y][x]:
                    res.append([y, x])
        return res

