#https://leetcode.com/problems/longest-palindromic-substring/submissions/

'''
Approaches
1> Brute 0n3
2> Run Two Pointers for even and odd palindromes  On2
3> Manacher 0n1.
'''

# Use Manacher
import operator
class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '^' + s.replace('','#') + '$'
        
        p = [0] * len(t)
        i = 1
        right = 0
        c = 0
        
        while i < len(t)-1:
            i_mirr = 2 * c - i
            
            if right > i:
                p[i] = min(right-i,p[i_mirr])
                
            while t[i +p[i] + 1] == t[i - p[i] - 1]:
                p[i]+=1
                
            if i > right:
                right = i + p[i]
                c = i
            
            i+=1
        
        c,p = max(enumerate(p),key=operator.itemgetter(1))
        
        start = (c - 1 -p)//2
        end = start + p
        
        return s[start:end]
                
        
        