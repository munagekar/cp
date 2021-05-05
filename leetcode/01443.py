class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        g = [[] for _ in range(n)]

        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        visited = set()
        visited.add(0)

        def dfs(n):

            weight = 0
            found = hasApple[n]

            for v in g[n]:
                if v in visited:
                    continue
                visited.add(v)
                f, w = dfs(v)
                if f:
                    found = True
                    weight += (w + 1)

            return found, weight

        found, weight = dfs(0)
        return weight * 2