# https://leetcode.com/problems/substring-with-concatenation-of-all-words/submissions/
from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        if len(words) == 0:
            return []
        
        # Dict of Words
        d = defaultdict(lambda : 0)
        
        for word in words:
            d[word]+=1
            
        
        len_word = len(words[0])
        tot_word_len = len_word * len(words)
        
        ans = []
        for i in range(0,len(s) - tot_word_len + 1):
            flag = True
            di = d.copy()
            for j in range(i,i+tot_word_len, len_word):
                word = s[j:j+len_word]
                
                if di[word] == 0:
                    flag = False
                    break
                    
                else:
                    di[word] -=1
                    
            if flag == True:
               ans.append(i)
            
        return ans