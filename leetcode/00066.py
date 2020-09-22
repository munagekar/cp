class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        res = []
        carry = 0
        digits = list(reversed(digits))
        digits[0] = digits[0] + 1
        for digit in digits:
            carry, digit = divmod(digit + carry, 10)
            res.append(digit)

        if carry:
            res.append(carry)
        return list(reversed(res))
