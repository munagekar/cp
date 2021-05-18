class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        s1 = (ay2 - ay1) * (ax2 - ax1)
        s2 = (by2 - by1) * (bx2 - bx1)

        ans = s1 + s2

        if ax1 >= bx2 or ay1 >= by2 or ax2 <= bx1 or ay2 <= by1:
            return ans

        bottom = max(ay1, by1)
        top = min(ay2, by2)
        left = max(ax1, bx1)
        right = min(ax2, bx2)

        return ans - (top - bottom) * (right - left)