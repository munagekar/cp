class UnionFind:

    def __init__(self, n):
        self.weights = [1] * n
        self.parents = list(range(0, n))

    def parent(self, x):
        while x != self.parents[x]:
            x = self.parents[x]
        return x

    def connect(self, x, y):
        x = self.parent(x)
        y = self.parent(y)

        if self.weights[x] < self.weights[y]:
            x, y = y, x

        self.weights[x] += self.weights[y]
        self.parents[y] = x


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        u = UnionFind(n)
        for (x, y) in edges:
            px = u.parent(x - 1)
            py = u.parent(y - 1)

            if px == py:
                return [x, y]

            u.connect(px, py)