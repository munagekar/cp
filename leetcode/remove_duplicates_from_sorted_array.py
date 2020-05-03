class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 1
        for n in nums:
            if n == nums[counter - 1]:
                continue
            nums[counter] = n
            counter += 1

        return counter