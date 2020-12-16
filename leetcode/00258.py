class Solution:
    def addDigits(self, num: int) -> int:
        if not num:
            return 0
        m = num %9
        if not m:
            return 9
        return m