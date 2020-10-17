class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = [
            12, 23, 34, 45, 56, 67, 78, 89,
            123, 234, 345, 456, 567, 678, 789,
            1234, 2345, 3456, 4567, 5678, 6789,
            12345, 23456, 34567, 45678, 56789,
            123456, 234567, 345678, 456789,
            1234567, 2345678, 3456789,
            12345678, 23456789,
            123456789
        ]

        return list(filter(lambda num: low <= num <= high, nums))


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        ans = []
        for i in range(1, 10):
            num = i
            digit = i + 1
            while num <= high and digit <= 10:
                if num >= low:
                    ans.append(num)

                num *= 10
                num += digit
                digit += 1

        return sorted(ans)
