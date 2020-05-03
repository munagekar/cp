class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        red = 0
        white = 1
        blue = 2

        (redp, whitep, bluep) = (0, 0, len(nums) - 1)

        while whitep <= bluep:

            if nums[whitep] == white:
                whitep += 1

            elif nums[whitep] == blue:
                nums[whitep], nums[bluep] = nums[bluep], nums[whitep]
                bluep -= 1

            else:
                nums[whitep], nums[redp] = nums[redp], nums[whitep]
                redp += 1
                whitep += 1