class Solution:
    def checkValidString(self, s: str) -> bool:
        cmax = cmin = 0

        for i in s:
            if i == "(":
                cmax += 1
                cmin += 1

            if i == ")":
                cmax -= 1
                cmin = max(0, cmin - 1)

            if i == "*":
                cmax += 1
                cmin = max(0, cmin - 1)

            if cmax < 0:
                return False

        return cmin == 0



