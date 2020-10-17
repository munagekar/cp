class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1

        for i in instructions:
            if i == "G":
                x, y = x + dx, y + dy

            elif i == "L":
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx

        return (x == 0 and y == 0) or (dy, dx) != (1, 0)