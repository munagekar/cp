class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <=0:
            return False
        while n != 1:
            if n % 3:
                return False
            else:
                n//=3
        return True

class Solution2:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3**19%n ==0