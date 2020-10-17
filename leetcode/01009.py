class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1

        digits = N.bit_length()
        return (1 << digits) - N - 1
