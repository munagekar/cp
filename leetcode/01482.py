class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def check(l, m, k, d):
            adj = 0
            p = 0
            for v in l:
                if v <= d:
                    adj += 1
                    if adj == k:
                        p += 1
                        adj = 0
                else:
                    adj = 0

            if p >= m:
                return True
            return False

        l = len(bloomDay)

        if k * m > l:
            return -1

        mini = min(bloomDay)
        maxi = max(bloomDay)

        if k * m == l:
            return maxi

        while mini < maxi:

            mid = (mini + maxi) // 2
            c = check(bloomDay, m, k, mid)
            if c:
                maxi = mid

            else:
                mini = mid + 1

        return maxi


