class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
        except:
            return False
        return True

# Regex : [-+]?(([0-9]+(.[0-9]*)?)|.[0-9]+)(e[-+]?[0-9]+)