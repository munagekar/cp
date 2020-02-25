# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/submissions/
from collections import defaultdict
from math import ceil
'''
Approach 1> Linear scan : ignores the fact the numbers were sorted.
Approach 2> Use the fact that the numbers are sorted. O(log(n))
'''


# Approach 1
# NOTE : Threre is no need for map since a simple size variable could have done the trick.
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        mapi = defaultdict(lambda : 0)
        
        target = int(len(arr) * 0.25) +1
        
        for num in arr:
            mapi[num]+=1
            if mapi[num] == target:
                return num

# Approach 2
def bounds(arr,index):
    # print("Search for",arr[index])
    num = arr[index]
    n = len(arr)
    # Max bound to check is index - n/4 +1, index + n/4 -1
    left_bound = max(0, index -n//4 -1)
    right_bound = min(n-1, index + n//4 + 1)
    
    # Implement Binary Search for search for left_bound
    
    low = left_bound
    high = index
    
    while low<high:
        # print("Leftbound",low,high)
        mid = (low + high) //2
        if arr[mid] < num:
            low = mid+1
        else:
            high = mid
            
    left_bound = low
    
    # Implement Binary Search for right_bound
    
    low = index
    high = right_bound
    while low< high:
        # print("Rightbound",low,high)
        mid = (low+high + 1)//2 # Tricky
        if arr[mid] > num:
            high = mid - 1
        else:
            low = mid
            
    right_bound = low
    
    return left_bound, right_bound
            
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        n4 = int(len(arr) * 0.25) 
        i = n4
        cut_off = len(arr)- n4 +1
        while i < cut_off:
            left_bound, right_bound = bounds(arr,i)
            if right_bound - left_bound + 1 > n4:
                return arr[i]
            
            i = right_bound +  n4