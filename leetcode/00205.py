class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_mapped = set()
        char_map = dict()

        if len(s) != len(t):
            return False

        for a, b in zip(s, t):
            if a not in char_map:
                if b in char_mapped:
                    return False
                char_map[a] = b
                char_mapped.add(b)

            else:
                if char_map[a] != b:
                    return False

        return True