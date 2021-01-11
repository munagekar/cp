import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        if not nums1 or not nums2:
            return []

        h = [(nums1[0] + nums2[0], 0, 0)]
        ans = []
        done = set()
        count = 0

        l1 = len(nums1)
        l2 = len(nums2)

        while count < k and h:
            v, i, j = heapq.heappop(h)
            ans.append([nums1[i], nums2[j]])
            count += 1

            if i + 1 < l1 and (i + 1, j) not in done:
                heapq.heappush(h, (nums1[i + 1] + nums2[j], i + 1, j))
                done.add((i + 1, j))

            if j + 1 < l2 and (i, j + 1) not in done:
                heapq.heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
                done.add((i, j + 1))

        return ans
    