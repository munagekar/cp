class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        nums = list(range(1, 10))
        if N == 1:
            nums.append(0)
            return nums
        for i in range(N - 1):
            newnums = []
            for n in nums:
                if n % 10 + K <= 9:
                    newnums.append(n * 10 + (n % 10) + K)
                if K and n % 10 - K >= 0:
                    newnums.append(n * 10 + (n % 10) - K)

            nums = newnums
            print(nums)

        return nums
