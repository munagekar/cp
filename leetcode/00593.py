class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2 == p3 == p4:
            return False

        ds = []
        for (x1, x2), (y1, y2) in itertools.combinations([p1, p2, p3, p4], 2):
            d = math.hypot(y1 - x1, y2 - x2)
            ds.append(d)

        ds = sorted(ds)

        if ds[0] == ds[1] == ds[2] == ds[3] and ds[4] == ds[5]:
            return True

        return False