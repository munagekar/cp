def area(p1, p2, p3):
    return 0.5 * abs(p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - p2[0] * p1[1] - p3[0] * p2[1] - p1[0] * p3[1])


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        a = 0
        for p1, p2, p3 in itertools.combinations(points, 3):
            a = max(a, area(p1, p2, p3))

        return a