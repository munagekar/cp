class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        l = len(nums)
        memo = {}

        def calculate(index, cur_sum):
            if index == l:
                if cur_sum == S:
                    return 1
                return 0

            if (index, cur_sum) in memo:
                return memo[(index, cur_sum)]

            pos = calculate(index + 1, cur_sum + nums[index])
            neg = calculate(index + 1, cur_sum - nums[index])

            tot = pos + neg

            memo[(index, cur_sum)] = tot
            return tot

        return calculate(0, 0)


class Solution2:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:

        count = defaultdict(int)
        count[0] = 1

        for x in nums:
            tmp = defaultdict(int)
            for y in count:
                tmp[y + x] += count[y]
                tmp[y - x] += count[y]
            count = tmp

        return count[S]