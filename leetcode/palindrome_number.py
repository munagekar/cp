
def reverse(x):
    ans = 0
    while x:
      d,m = divmod(x,10)
      ans *= 10
      ans += m
      x = d
    return ans

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        if x  == 0:
            return True
        
        return x == reverse(x)
            
        