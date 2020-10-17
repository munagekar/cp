def mcap(x):
    return max(x, 0)


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days = set(days)

        d = [math.inf] * 366
        d[0] = 0
        c0 = 0
        c1, c7, c30 = costs

        for i in range(1, 366):
            if i not in days:
                d[i] = d[i - 1]
            else:
                d[i] = min(d[i], d[i - 1] + c1, d[mcap(i - 7)] + c7, d[mcap(i - 30)] + c30)

        return d[365]