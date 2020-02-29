# https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Zig Zag Cycle Length = 2n -2
        n = numRows
        if s is None or s =='':
            return ''
        
        if numRows == 1:
            return s
        
        
        first_row = s[:: 2 * n -2]
        
        last_row = s[n-1::2* n -2]
        
        ans = [first_row]
        
        for r in range(1,n-1):
            index = r
            while True:
                if index >= len(s):
                    break
                ans.append(s[index])

                index2 = index + 2 * (n -r -1)
                if index2 >=len(s):
                    break
                ans.append(s[index2])
                index +=  2 * n -2
                
        ans.append(last_row)
        return ''.join(ans)