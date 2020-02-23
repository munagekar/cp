# https://leetcode.com/problems/regular-expression-matching/submissions/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def dp(i,j):
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            
            if j == len(p):
                flag = i==len(s)
                memo[(i,j)] = flag
                return flag
                    
            first_match = i < len(s) and (p[j] =='.' or p[j] == s[i])
                    
            if j < len(p)-1 and p[j+1] =='*':
                dp_ans = dp(i,j+2) or (first_match and dp(i+1,j))
            else:
                dp_ans = (first_match and dp(i+1,j+1))
            
            memo[(i,j)] = dp_ans    
            return memo[(i,j)]
    
        return dp(0,0)