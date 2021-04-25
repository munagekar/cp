class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        g = [[] for _ in range(n)]

        ranks = [-1] * n
        low = [-1] * n

        current_rank = 0
        prev = -1
        res = []

        for x, y in connections:
            g[x].append(y)
            g[y].append(x)

        def dfs(prev, current, rank):
            ranks[current] = rank

            for v in g[current]:
                if v == prev:
                    continue

                if ranks[v] == -1:
                    dfs(current, v, rank + 1)

                ranks[current] = min(ranks[current], ranks[v])

                if ranks[v] >= rank + 1:
                    res.append([v, current])

        dfs(-1, 0, 0)
        return res