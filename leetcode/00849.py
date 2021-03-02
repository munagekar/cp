class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        occ = []

        for i, s in enumerate(seats):
            if s == 1:
                occ.append(i)

        ans = max(occ[0], len(seats) - 1 - occ[-1])

        if len(occ) == 1:
            return ans

        for x, y in zip(occ, occ[1:]):
            d = (y - x) // 2
            ans = max(d, ans)

        return ans