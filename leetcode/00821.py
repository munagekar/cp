class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        occ = [i for i, v in enumerate(s) if v == c]

        occ = [-math.inf] + occ + [math.inf]

        index = 0

        res = []
        for i, v in enumerate(s):
            if v == c:
                res.append(0)
                index += 1
            else:
                res.append(min(abs(i - occ[index]), abs(i - occ[index + 1])))

        return res