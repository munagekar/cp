class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:

        ans = [[0] * len(colsum) for _ in range(2)]

        for i, s in enumerate(colsum):
            if s == 2:
                ans[1][i] = 1
                ans[0][i] = 1
                upper -= 1
                lower -= 1

        for i, s in enumerate(colsum):
            if s == 1:
                if upper >= 1:
                    ans[0][i] = 1
                    upper -= 1
                elif lower >= 1:
                    ans[1][i] = 1
                    lower -= 1
                else:
                    return []

        if upper != 0 or lower != 0:
            return []

        return ans