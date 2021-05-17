class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def resolve(s):
            ans = []
            for c in s:
                if c == "#":
                    if len(ans) == 0:
                        continue
                    ans.pop()
                else:
                    ans.append(c)
            return ans

        return resolve(s) == resolve(t)


class Solution2:
    def backspaceCompare(self, s: str, t: str) -> bool:

        si = len(s) - 1
        ti = len(t) - 1

        counts = 0
        countt = 0

        while si >= 0 or ti >= 0:

            while si >= 0:
                if s[si] == "#":
                    counts += 1
                    si -= 1

                elif counts > 0:
                    counts -= 1
                    si -= 1

                else:
                    break

            while ti >= 0:
                if t[ti] == "#":
                    countt += 1
                    ti -= 1

                elif countt > 0:
                    countt -= 1
                    ti -= 1

                else:
                    break

            if si >= 0 and ti < 0:
                return False

            elif si < 0 and ti >= 0:
                return False

            if s[si] != t[ti]:
                return False

            si -= 1
            ti -= 1

        return True



