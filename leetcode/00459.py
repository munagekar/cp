class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        for i in range(l // 2, 0, -1):
            if l % i:
                continue

            cons = s[:i] * (l // i)
            if cons == s:
                return True
        return False


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]