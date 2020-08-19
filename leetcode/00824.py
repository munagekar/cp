class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split(' ')
        v = set(["a","e","i","o","u","A","E","I","O","U"])
        res = []
        for i,w in enumerate(words,1):
            suffix = "a"*i
            if w[0] in v:
                w = w + "ma"
            else:
                w = w[1:] + w[0] + "ma"
                
            res.append(w+suffix)
            
        return " ".join(res)
