from itertools import zip_longest
from functools import cmp_to_key


def cmp(a, b):
    if a + b > b + a:
        return 1
    else:
        return -1


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = map(str, nums)
        nums = sorted(nums, key=cmp_to_key(cmp), reverse=True)
        nums = "".join(nums)
        return nums.lstrip("0") or "0"