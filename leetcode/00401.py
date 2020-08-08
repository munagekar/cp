from itertools import combinations


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:

        res = []

        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == num:
                    res.append(f"{h}:{m:02d}")

        return res


from itertools import combinations


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:

        if not num:
            return ["0:00"]

        res = []

        for h in range(min(3, num) + 1):
            hopts = [sum(x) for x in combinations([1, 2, 4, 8], h) if sum(x) < 12]
            if h == 0:
                hopts = [0]
            m = min(6, num - h)
            mopts = [sum(m) for m in combinations([1, 2, 4, 8, 16, 32], m) if sum(m) < 60]
            if m == 0:
                mopts = [0]
            for hourop, minop in itertools.product(hopts, mopts):
                res.append(f"{hourop}:{minop:02d}")

        return sorted(res)



