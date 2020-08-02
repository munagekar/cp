from string import ascii_lowercase


def path(y1, x1, y2, x2):
    """
    To handle path handling complexity better to LU before DR
    """
    path = ""
    if (y1, x1, y2, x2) == (5, 0, 5, 0):
        return ""

    if (y1, x1) == (5, 0):
        path += "U"
        y1, x1 = 4, 0

    special_flag = False
    if (y2, x2) == (5, 0):
        y2, x2 = 4, 0
        special_flag = True

    if y2 > y1:
        path += "D" * (y2 - y1)

    elif y1 > y2:
        path += "U" * (y1 - y2)

    if x2 > x1:
        path += "R" * (x2 - x1)

    elif x2 < x1:
        path += "L" * (x1 - x2)

    if special_flag:
        path += "D"
    return path


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        pos_map = {char: divmod(x, 5) for x, char in enumerate(ascii_lowercase)}
        print(pos_map)
        prev = (0, 0)

        ans = ""

        for char in target:
            cur = pos_map[char]
            ans += path(*prev, *cur) + "!"
            prev = cur

        return ans


