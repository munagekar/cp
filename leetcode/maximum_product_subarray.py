# https://leetcode.com/problems/maximum-product-subarray/

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = nums
        neg = arr[0]
        pos = arr[0]
        target = arr[0]
        for val in arr[1:]:
            if val >= 0:
                pos *= val
                pos = max(pos, val)
                neg *= val
            if val < 0:
                pos, neg = neg, pos
                pos *= val
                neg *= val
                neg = min(neg, val)
            target = max(pos, target)

        return target
        