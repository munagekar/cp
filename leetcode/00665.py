class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        i = 1
        done = False
        while i <= len(nums) - 1:

            if nums[i] < nums[i - 1]:
                if done:
                    return False
                done = True

                if i - 2 < 0 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
            i += 1
        return True