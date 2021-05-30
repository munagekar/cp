class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        r = 1
        ans = nums[0]
        c = nums[0]
        s = {nums[0]}

        while r < len(nums):
            if nums[r] not in s:
                s.add(nums[r])
                c += nums[r]
                ans = max(c, ans)
                r += 1

            else:
                while nums[l] != nums[r]:
                    s.remove(nums[l])
                    c -= nums[l]
                    l += 1
                s.remove(nums[l])
                c -= nums[l]
                l += 1

        return ans
