class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        first = n %2
        n = n//2
        while n !=0:
            current = n %2
            if first == current:
                return False
            first = current
            n//=2
        return True