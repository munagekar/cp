class Solution:
    def findNthDigit(self, n: int) -> int:

        if n <= 9:
            return n
        boxes = []

        num = 0
        counter = 1
        multiplier = 1
        maxi = 2 ** 31
        while num <= maxi:
            num = 9 * multiplier * counter
            boxes.append(num)
            multiplier *= 10
            counter += 1

        # print(boxes)

        digits = 1
        while n > boxes[0]:
            n -= boxes.pop(0)
            digits += 1

        # print(digits)
        # print(n)

        base = 10 ** (digits - 1)
        selector, digit = divmod(n - 1, digits)
        # print(selector,digit)

        num = base + selector
        # print(num)
        return int(str(num)[digit])
