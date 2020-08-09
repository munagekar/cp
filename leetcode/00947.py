class UF:

    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n

    def connect(self, first, second):
        fp = self.root(first)
        fs = self.size[fp]

        sp = self.root(second)
        ss = self.size[sp]

        if fs >= ss:
            self.parents[sp] = fp
        else:
            self.parents[fp] = sp

    def root(self, vertex):
        while self.parents[vertex] != vertex:
            vertex = self.parents[vertex]

        return vertex


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        row_dict = collections.defaultdict(list)
        col_dict = collections.defaultdict(list)

        uf = UF(len(stones))

        for i, (x, y) in enumerate(stones):
            for v in row_dict[y]:
                uf.connect(i, v)
                break
            for v in col_dict[x]:
                uf.connect(i, v)
                break
            row_dict[y].append(i)
            col_dict[x].append(i)

        #         print(row_dict)
        #         print(col_dict)
        #         print(uf.parents)
        return len(stones) - sum(i == x for (i, x) in enumerate(uf.parents))



