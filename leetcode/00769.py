class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        diffs = [val - i for i, val in enumerate(arr)]

        chunks = 0
        chunk_end = 0
        for i, diff in enumerate(diffs):
            chunk_end = max(chunk_end, i + diff)
            if i == chunk_end:
                chunks += 1
                chunk_end += 1

        return chunks