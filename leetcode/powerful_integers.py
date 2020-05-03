class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:

        if x == 1 and y == 1:
            return [2] if bound >= 2 else []

        ans = set()

        if y == 1:
            y, x = x, y

        if x == 1:
            powy = 0
            while True:
                test = y ** powy + 1
                if test <= bound:
                    ans.add(test)
                    powy += 1
                else:
                    return list(ans)

        powx = 0

        while True:
            testx = x ** powx
            powx += 1
            if testx > bound:
                return list(ans)
            powy = 0
            while True:
                testy = y ** powy
                sol = testx + testy
                if sol > bound:
                    break
                else:
                    ans.add(sol)
                    powy += 1
