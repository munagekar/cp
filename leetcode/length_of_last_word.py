class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        try:
            return len(s) - s.rindex(' ') -1
        except:
            return len(s)