class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c,r,o,a,k = [0]*5
        ans = 0
        for char in croakOfFrogs:

            ans = max(ans,c)
            
            if char == 'c':
                c += 1
            
            elif char == "r":
                r+=1
                
            elif char == "o":
                o+=1
                
            elif char == "a":
                a+=1
                
            elif char == 'k':
                c -=1
                r -=1
                o -=1
                a -=1
                
            if c<r or r<o or o<a or a<k:
                return -1
        
        if c!=0:
            return -1
        
        return ans
