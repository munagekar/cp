class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s= re.sub(r"[ ]+"," ",s)
        return ' '.join(list(reversed(s.split())))