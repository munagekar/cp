class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        q = collections.deque()
        q.append([beginWord, 1])

        while q:

            w, l = q.popleft()

            if w == endWord:
                return l

            for i in range(len(w)):
                for c in string.ascii_lowercase:
                    n = w[:i] + c + w[i + 1:]
                    if n in word_set:
                        word_set.remove(n)
                        q.append((n, l + 1))
        return 0