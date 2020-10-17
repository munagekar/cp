# Boyer-moore voting algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        ans = nums[0]
        count = 1

        for n in nums[1:]:
            if n != ans:
                count -= 1
                if count == 0:
                    ans = n
                    count = 1
            else:
                count += 1

        return ans
