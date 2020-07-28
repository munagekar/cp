from itertools import islice
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        maxlen = min(map(len,strs))
        
        for i in range(maxlen):
            c = strs[0][i]
            if not all(s[i] == c for s in islice(strs,1,len(strs))):
                return strs[0][:i]
            
        return strs[0][:maxlen]