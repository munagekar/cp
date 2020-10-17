class Solution:
    def smallestSubsequence(self, chars: str) -> str:

        d = defaultdict(lambda: -1)

        # Build last occurance
        for i, c in enumerate(chars):
            if i > d[c]:
                d[c] = i

        s = list()
        seti = set()

        for i, c in enumerate(chars):
            if c in seti:
                continue
            while s and s[-1] >= c and d[s[-1]] >= i:
                seti.remove(s.pop())
            s.append(c)
            seti.add(c)

        return "".join(s)