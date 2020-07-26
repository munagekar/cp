class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0
        p = 0
        while si < len(s) and p < len(t):
            if t[p] == s[si]:
                si += 1

            p += 1

        return si == len(s)


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        return all(c in t for c in s)