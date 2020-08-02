from itertools import islice


def sort_function2(a):
    return a[0], -a[1]


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=sort_function2)
        max_seen = intervals[0][1]
        count = 1
        for [mini, maxi] in intervals[1:]:
            if maxi <= max_seen:
                continue
            max_seen = max(max_seen, maxi)
            count += 1

        return count