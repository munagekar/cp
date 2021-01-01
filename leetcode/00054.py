class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        t = 0
        b = len(matrix) - 1

        l = 0
        r = len(matrix[0]) - 1

        dir = 0
        res = []

        while (t <= b and l <= r):

            if dir == 0:
                for i in range(l, r + 1):
                    res.append(matrix[t][i])
                t += 1

            if dir == 1:
                for i in range(t, b + 1):
                    res.append(matrix[i][r])
                r -= 1

            if dir == 2:
                for i in range(r, l - 1, -1):
                    res.append(matrix[b][i])
                b -= 1

            if dir == 3:
                for i in range(b, t - 1, -1):
                    res.append(matrix[i][l])
                l += 1

            dir += 1
            dir %= 4

        return res