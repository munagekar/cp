class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        heights.append(0)
        s = []

        ans = 0

        for i, h in enumerate(heights):
            if len(s) == 0 or h > heights[s[-1]]:
                s.append(i)
                continue

            while s and h < heights[s[-1]]:
                tp = s.pop()

                if not s:
                    width = i
                else:
                    width = i - 1 - s[-1]

                ans = max(width * heights[tp], ans)

            s.append(i)

        return ans