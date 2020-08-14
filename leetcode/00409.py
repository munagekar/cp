class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        
        counts = collections.Counter(s)
        
        ans = 0
        for x,y in counts.items():
            ans += (y//2) * 2
            
        if ans !=len(s):
            ans += 1
            
        return ans 
