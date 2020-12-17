class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        c = collections.Counter(a+b for a in A for b in B)
        return sum(c[-x -y] for x in C for y in D)