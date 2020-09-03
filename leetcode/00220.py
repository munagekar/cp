from collections import OrderedDict


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        buckets = OrderedDict()
        if k < 1 or t < 0:
            return False

        for v in nums:
            idx = v // t if t else v
            for m in (buckets.get(idx), buckets.get(idx - 1), buckets.get(idx + 1)):
                if m is not None and abs(m - v) <= t:
                    return True

            if len(buckets) == k:
                buckets.popitem(False)

            buckets[idx] = v

        return False
