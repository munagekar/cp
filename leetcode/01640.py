class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        m = {x[0]: x for x in pieces}

        res = []
        for a in arr:
            res += m.get(a, [])

        return res == arr
