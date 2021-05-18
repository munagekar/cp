class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        idx = 0
        l = len(bits)
        while idx < l - 1:
            if bits[idx] == 1:
                idx += 2
            else:
                idx += 1

        if idx == l - 1:
            return True
        return False