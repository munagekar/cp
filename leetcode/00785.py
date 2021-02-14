class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        NC = 0
        G = 1
        B = -1
        c = [NC] * len(graph)

        def dfs(v, graph, color):
            if c[v] != NC:
                return True

            c[v] = color

            for n in graph[v]:

                if c[n] == color:
                    return False

                if c[n] == NC and not dfs(n, graph, -color):
                    return False

            return True

        return all(dfs(v, graph, G) for v in range(len(graph)))