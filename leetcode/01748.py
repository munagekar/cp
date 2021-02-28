class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        return sum((k for k in c if c[k]==1))