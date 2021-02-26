class Solution:
    def scoreOfParentheses(self, S: str) -> int:

        l = 0
        ans = 0
        for i, c in enumerate(S):
            if c == '(':
                l += 1
            else:
                l -= 1
                if S[i - 1] == "(":
                    ans += 1 << l

        return ans


class Solution2:
    def scoreOfParentheses(self, S: str) -> int:

        s = []

        for c in S:
            if c == "(":
                s.append("(")

            else:
                cur = 0
                while s[-1] != "(":
                    cur += s.pop()
                s.pop()
                if cur == 0:
                    cur = 1
                else:
                    cur = cur * 2
                s.append(cur)

        return sum(s)
