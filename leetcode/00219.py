class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}

        for i, n in enumerate(nums):
            j = m.get(n)
            if j is not None and i - j <= k:
                return True
            m[n] = i

        return False