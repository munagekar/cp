class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        s = []
        d = collections.defaultdict(lambda: -1)

        for n in nums2:
            while len(s) != 0 and n > s[-1]:
                d[s.pop()] = n

            s.append(n)

        return [d[x] for x in nums1]