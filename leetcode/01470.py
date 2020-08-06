class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        l = len(nums)//2
        for x in range(l):
            res.append(nums[x])
            res.append(nums[x+l])
        return res