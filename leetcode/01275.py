def check(b, p):
    for y in range(0, 3):
        if all(b[x][y] == p for x in range(0, 3)):
            return True

    for x in range(0, 3):
        if all(b[x][y] == p for y in range(0, 3)):
            return True

    if b[0][0] == p and b[1][1] == p and b[2][2] == p:
        return True

    if b[0][2] == p and b[1][1] == p and b[2][0] == p:
        return True

    return False


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        b = [["."] * 3 for _ in range(3)]

        for ((x, y), p) in zip(moves, itertools.cycle("AB")):
            b[x][y] = p

        if check(b, "A"):
            return "A"

        if check(b, "B"):
            return "B"

        if len(moves) == 9:
            return "Draw"

        return "Pending"