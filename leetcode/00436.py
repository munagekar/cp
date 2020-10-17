class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        search = sorted(((x[0], i) for i, x in enumerate(intervals)))
        l = len(intervals)

        res = []
        for _, x in intervals:
            index = bisect.bisect_right(search, (x,))
            if index == l:
                res.append(-1)
            else:
                res.append(search[index][1])

        return res