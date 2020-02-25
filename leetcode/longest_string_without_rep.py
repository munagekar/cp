# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Approach Sliding Window
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indices = defaultdict(lambda : -1)
        
        max_length = 0
        start_index = 0
        running_length = 0
        for idx,char in enumerate(s):
            last_index = indices[char]
            if last_index!=-1:
                running_length = idx - last_index
                
                # Deleting Characters
                for i in range(start_index,last_index+1):
                    indices[s[i]]=-1
                    
                indices[char] = idx
                start_index = last_index+1
            else:
                running_length +=1
                max_length = max(max_length,running_length)
                indices[char]=idx
                
        return max_length
            