class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:

        m = max(instructions)
        bit = [0] * (m + 1)

        def u(x):
            while x <= m:
                bit[x] += 1
                x += x & -x

        def g(x):
            s = 0
            while x > 0:
                s += bit[x]
                x -= x & -x
            return s

        ans = 0
        for i, v in enumerate(instructions):
            ans += min(g(v - 1), i - g(v))
            u(v)

        return ans % (10 ** 9 + 7)