'''
https://leetcode.com/problems/two-sum/

Approach one : nlogn + nlogn
For every number binary search sorted array

Approach two Used: nlogn + n 
Two Pointer first,last in sorted array

Approach three: Linear
Use Map, Check if number complement is present else insert number
Eg: If on 2 and target is 7, check for 5.
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first = 0
        last = len(nums) - 1
        
        nums.sort()
        
        while True:
            check = nums[first] + nums[last]
            if check == target:
                return [first,last]
            elif check > target:
                last-=1
            else:
                first+=1