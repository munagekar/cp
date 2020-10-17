class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []
        ns, ne = newInterval

        if not intervals:
            return [newInterval]

        for i, (s, e) in enumerate(intervals):
            if e < ns:
                res.append((s, e))

            elif ne < s:
                i -= 1
                break

            else:
                ns, ne = min(s, ns), max(e, ne)

        res.append([ns, ne])
        res.extend(intervals[i + 1:])

        return res