class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        if l % k != 0:
            return False

        nums = Counter(nums)

        for num in sorted(nums):
            occurance = nums[num]
            if occurance:
                for num2 in range(num + 1, num + k):
                    if nums[num2] < occurance:
                        return False
                    nums[num2] -= occurance
        return True