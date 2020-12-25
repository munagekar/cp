class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix:
            return []

        r = len(matrix)
        c = len(matrix[0])

        le = r * c
        l = []
        i = 0

        n = 0
        m = 0

        while i < le:

            l.append(matrix[n][m])
            i += 1

            if (n + m) % 2 == 0:
                if m == c - 1:
                    n += 1

                elif n == 0:
                    m += 1

                else:
                    n -= 1
                    m += 1

            else:
                if n == r - 1:
                    m += 1
                elif m == 0:
                    n += 1
                else:
                    n += 1
                    m -= 1
        return l