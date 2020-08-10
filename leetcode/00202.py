def get_digits(n):
    d = []
    while n:
        d.append(n % 10)
        n //= 10
    return d


class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        nums.add(n)

        while True:
            digits = get_digits(n)
            n = sum(d * d for d in digits)
            if n == 1:
                return True
            if n in nums:
                return False

            nums.add(n)

