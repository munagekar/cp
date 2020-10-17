class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n1, n2, c1, c2 = 0, 1, 0, 0

        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
            elif c1 <= 0:
                c1 = 1
                n1 = num
            elif c2 <= 0:
                c2 = 1
                n2 = num
            else:
                c1 -= 1
                c2 -= 1

        return [x for x in [n1, n2] if nums.count(x) > len(nums) / 3]
