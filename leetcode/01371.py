class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        m = {0: -1}
        v = 0
        cm = {}
        cm['a'] = 0
        cm['e'] = 1
        cm['i'] = 2
        cm['o'] = 3
        cm['u'] = 4

        a = -1

        for i, c in enumerate(s):
            pos = cm.get(c)
            if pos is not None:
                v ^= 1 << pos

            m.setdefault(v, i)
            a = max(a, i - m[v])

        return a
