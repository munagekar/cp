class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mapi = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        def trans(w):
            ret = [mapi[ord(c) - ord('a')] for c in w]
            return "".join(ret)

        c = {x for x in map(trans, words)}
        return len(c)