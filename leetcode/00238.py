class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = list(itertools.accumulate(nums, operator.mul))
        left_product = [1] + left_product

        right_product = list(reversed(list(itertools.accumulate(reversed(nums), operator.mul))))
        right_product = right_product + [1]

        res = []

        for i in range(len(nums)):
            res.append(left_product[i] * right_product[i + 1])

        return res