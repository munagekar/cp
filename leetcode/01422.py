class Solution:
    def maxScore(self, s: str) -> int:
        l = len(s)
        zeroes = []
        ones = []

        z, o = 0, 0
        for x in s:
            if x == '0':
                z += 1

            else:
                o += 1
            zeroes.append(z)
            ones.append(o)
        ans = -1
        for i in range(1, l):
            s = zeroes[i - 1] + ones[l - 1] - ones[i - 1]
            ans = max(s, ans)

        return ans