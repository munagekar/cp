class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        l = len(s)

        m = [[False] * l for _ in range(l)]
        count = 0

        for i in range(l):
            m[i][i] = True
            count += 1

        for i in range(l - 1):
            if s[i] == s[i + 1]:
                m[i][i + 1] = True
                count += 1

        for k in range(2, l):
            for i in range(0, l - k):
                if s[i] == s[i + k] and m[i + 1][i + k - 1]:
                    count += 1
                    m[i][i + k] = True

        return count
