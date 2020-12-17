class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = len(T) * [0]

        stack = []

        for i in range(len(T) - 1, -1, -1):
            while len(stack) > 0 and T[i] >= T[stack[-1]]:
                stack.pop()

            if len(stack) != 0:
                ans[i] = stack[-1] - i
            stack.append(i)

        return ans