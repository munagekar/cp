class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        g = collections.defaultdict(dict)
        for (var1, var2), val in zip(equations, values):
            g[var1][var1] = 1
            g[var2][var2] = 1
            g[var1][var2] = val
            g[var2][var1] = (1 / val)

        for k in g:
            for i, j in itertools.permutations(g[k], 2):
                g[i][j] = g[i][k] * g[k][j]

        return [g[a].get(b, -1) for (a, b) in queries]