class Solution:

    def find132pattern(self, nums: List[int]) -> bool:

        s3 = -math.inf
        s = list()

        for n in reversed(nums):
            if n < s3:
                return True

            while (len(s) > 0 and s[-1] < n):
                s3 = s.pop()

            s.append(n)

        return False
