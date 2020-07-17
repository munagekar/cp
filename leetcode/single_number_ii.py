class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        msb = 0
        lsb = 0
        for num in nums:
            lsb = (lsb ^ num) & ~msb
            msb = (msb ^ num) & ~lsb

        return lsb


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        res = 0
        bit_mask = 1
        num_neg = sum(i < 0 for i in nums) % 3
        sign = 1 if not num_neg else -1

        for i in range(32):
            bit = 0
            for num in nums:
                if sign == 1 and num > 0:
                    bit += (num & bit_mask) >> i
                if sign == -1 and num < 0:
                    num *= -1
                    bit += (num & bit_mask) >> i

            bit %= 3
            res += bit << i
            bit_mask *= 2

        return res * sign