class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        stops = [0] * 1001

        for n, s, e in trips:
            stops[s] += n
            stops[e] -= n

        for s in stops:
            capacity -= s
            if capacity < 0:
                return False

        return True