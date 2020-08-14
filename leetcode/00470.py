# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        n =50
        while n > 40:
            n = (rand7()-1)*7 + rand7()
            
        return (n-1)//4 + 1
        
