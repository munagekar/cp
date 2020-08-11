class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse=True)
        l = len(citations)
        ans = 0
        for i, h in enumerate(citations):
            ans = max(min(i + 1, h), ans)

        return ans


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))
