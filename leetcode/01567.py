class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        pos = [0] * len(nums)
        neg = [0] * len(nums)

        if nums[0] > 0:
            pos[0] = 1
        elif nums[0] < 0:
            neg[0] = 1

        ans = pos[0]

        for i, n in enumerate(nums[1:], 1):
            if n > 0:
                pos[i] = pos[i - 1] + 1
                neg[i] = neg[i - 1] + 1 if neg[i - 1] > 0 else 0

            if n < 0:
                pos[i] = neg[i - 1] + 1 if neg[i - 1] > 0 else 0
                neg[i] = pos[i - 1] + 1

            ans = max(ans, pos[i])

        return ans



