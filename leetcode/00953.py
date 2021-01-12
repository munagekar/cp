class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {c: i for i, c in enumerate(order)}

        def c(x, y):
            for i, j in zip(x, y):
                if order[i] > order[j]:
                    return False
                if order[j] > order[i]:
                    return True
            if len(x) <= len(y):
                return True
            return False

        return all(c(x, y) for x, y in zip(words, words[1:]))
