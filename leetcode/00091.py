class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        m = {}
        
        def solve(s):
            if len(s) >0 and s[0] == '0':
                return 0
            
            if len(s) <=1:
                return 1
            
            x = m.get(s)
            if x:
                return x

            if s[0] == '1':
                m[s] = solve(s[1:]) + solve(s[2:])

            elif s[0] == '2' and int(s[1]) <=6:
                m[s]=solve(s[1:]) + solve(s[2:])
            else:
                m[s]= solve(s[1:])
                
            return m[s]

        return solve(s)
                
        
