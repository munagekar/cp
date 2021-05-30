class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        if len(s) < minSize:
            return 0
        if len(s) == minSize:
            return 1

        d = defaultdict(lambda: 0)
        sub = s[:minSize]
        d[sub] += 1

        for x in s[minSize:]:
            sub = sub[1:] + x
            d[sub] += 1

        l = sorted([(v, k) for k, v in d.items()], reverse=True)

        for v, k in l:
            if len(set(k)) <= maxLetters:
                return v

        return 0

