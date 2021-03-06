class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        good = set(words)
        for w in words:
            for i in range(1, len(w)):
                good.discard(w[i:])

        return sum(len(w) + 1 for w in good)