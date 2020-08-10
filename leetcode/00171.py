from string import ascii_uppercase

base26 = {y: x for x, y in enumerate(ascii_uppercase, 1)}


class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for char in s:
            res *= 26
            res += base26[char]

        return res