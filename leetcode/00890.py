class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def sign(x):
            s = []
            i = 0
            m = {}
            for c in x:
                if c in m:
                    s.append(m[c])
                else:
                    s.append(i)
                    m[c] = i
                    i += 1

            return s

        s = sign(pattern)

        return [x for x in words if sign(x) == s]