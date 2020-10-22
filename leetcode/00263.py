class Solution:
    def isUgly(self, num: int) -> bool:
        if num < 1:
            return False
        if num <= 6:
            return True

        for n in [2, 3, 5]:
            while num % n == 0:
                num //= n
                print(num)

        if num == 1:
            return True

        return False
