class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for lp,l in zip(triangle,triangle[1:]):
            length = len(l)
            for i in range(length):
                l[i] = l[i] + min(lp[max(i-1,0)],lp[min(i,length-2)])
        return min(triangle[-1])