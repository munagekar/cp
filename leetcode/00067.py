class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]


from itertools import zip_longest


class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        c = 0
        ans = []
        for x, y in zip_longest(reversed(a), reversed(b), fillvalue='0'):
            c, s = divmod(int(x) + int(y) + c, 2)
            ans.append(str(s))

        if c:
            ans.append(str(c))

        return "".join(reversed(ans))