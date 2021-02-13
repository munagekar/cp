class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        m = {0: -1}
        v = 0
        cm = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

        a = -1

        for i, c in enumerate(s):
            pos = cm.get(c)
            if pos is not None:
                v ^= 1 << pos

            m.setdefault(v, i)
            a = max(a, i - m[v])

        return a
