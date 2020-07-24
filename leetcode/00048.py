def transpose(m):
    l = len(m)

    print(m)

    for i in range(0, l - 1):
        for j in range(i + 1, l):
            m[i][j], m[j][i] = m[j][i], m[i][j]

    return m


def flip(m):
    for i in range(0, len(m)):
        m[i] = m[i][::-1]


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        flip(transpose(matrix))