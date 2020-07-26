# https://leetcode.com/problems/reverse-integer/
'''
Approach 1 > Convert to string and reverse.
Approach 2> Used. 
NOTE: For Buffer Overflow You need to check if x becomes negative
not implemented properly, since no issues with python
'''

class Solution:
    def reverse(self, x: int) -> int:
        negative = True if x < 0 else False
        if negative:
            x = -x
        
        ans = 0
        while x>0:
            ans *=10
            ans += x%10
            x//=10
            
        if negative:
            ans *=-1
            
        if ans < -(2**31) or ans >= 2**31:
            ans = 0
        
        return ans