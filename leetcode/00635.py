class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        x = sum(set(nums))
        y = (len(nums)*(len(nums)+1))//2
        return [sum(nums)-x,y-x]