from collections import OrderedDict, Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = OrderedDict()

        for i, c in enumerate(s):
            if c in d:
                d[c] = -1
            else:
                d[c] = i

        for v in d.values():
            if v != -1:
                return v

        return -1

    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)

        for i, char in enumerate(s):
            if c[char] == 1:
                return i

        return -1