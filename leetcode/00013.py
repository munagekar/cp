# https://leetcode.com/problems/roman-to-integer/
d = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}


class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0 or s == '':
            return 0

        index = 0
        num = 0

        l = len(s)

        while index < l:
            val = None
            if index + 1 < l:
                val = d.get(s[index:index + 2])

                if val == None:
                    val = d.get(s[index])
                    index += 1
                else:
                    index += 2
            else:
                val = d.get(s[index])
                index += 1

            num += val

        return num