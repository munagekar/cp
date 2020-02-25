import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s= s.lower()
        regex = re.compile('[^a-z0-9]')
        s = regex.sub('',s)
        if s == s[::-1]:
            return True
        return False