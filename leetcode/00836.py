class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:

        x1, y1, x2, y2 = rec1
        xi1, yi1, xi2, yi2 = rec2

        if x1 == x2 or y1 == y2 or xi1 == xi2 or yi1 == yi2:
            return False

        # rec2 right

        if xi1 >= x2:
            return False

        # rec2 left

        if xi2 <= x1:
            return False

        # rec2 top

        if yi1 >= y2:
            return False

        # rec2 bottom

        if yi2 <= y1:
            return False

        return True
