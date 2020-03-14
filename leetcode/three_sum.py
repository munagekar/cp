class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        i = 0
        
        res = []
        # print(nums)
        while i < l -2:
            num = nums[i]
            # print(f"Trying {i} {num}")
            if num >0:
                break
                
            # print("Trying 2 Sum")
            # Reduce the problem to 2 Sum
            left = i + 1
            right = l -1
            
            while i< right and left < l and left < right:
                left_num = nums[left]
                right_num = nums[right]
                # print(f"Try {left_num} {right_num}")
                if left_num + right_num + num == 0:
                    res.append([num,left_num,right_num])
                    
                    # Remove Duplicates
                    while left < l and nums[left] ==left_num:
                        left+=1
                        
                    # Correct Overshoot
                    left -=1
                    while right > i and nums[right] == right_num:
                        right-=1
                        
                elif left_num + right_num + num > 0:
                    right -=1
                    
                else:
                    left +=1
                    
            while i<l-1 and nums[i]==nums[i+1]:
                i+=1
            i+=1
        return res