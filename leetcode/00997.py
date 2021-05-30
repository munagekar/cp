class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        t_count = {i: 0 for i in range(1, n + 1)}

        candidates = set(list(range(1, n + 1)))

        for p, t in trust:
            t_count[t] += 1
            candidates.discard(p)

        for c in candidates.copy():
            if t_count[c] != n - 1:
                candidates.discard(c)

        if len(candidates) != 1:
            return -1

        return candidates.pop()
