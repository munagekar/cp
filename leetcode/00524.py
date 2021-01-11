class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:

        ls = len(s)

        def is_sub(y):
            j = 0
            i = 0

            ly = len(y)

            while i < ls and j < ly:
                if s[i] == y[j]:
                    j += 1
                i += 1

            if j == ly:
                return True

            return False

        ans = ""
        for x in d:
            if is_sub(x):
                if len(x) > len(ans):
                    ans = x
                elif len(x) == len(ans) and x < ans:
                    ans = x

        return ans