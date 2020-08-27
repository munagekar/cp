class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        if not pairs:
            return 0

        pairs.sort(key=operator.itemgetter(1))

        end = pairs[0][1]
        count = 1
        for s, e in pairs[1:]:
            if s > end:
                end = e
                count += 1

        return count