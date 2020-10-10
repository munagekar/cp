class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points = sorted(points)
        count = 1
        if not points:
            return 0

        maxi = points[0][1]

        for p in points[1:]:
            if maxi < p[0]:
                count += 1
                maxi = p[1]
            else:
                maxi = min(maxi, p[1])

        return count