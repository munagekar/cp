class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)

        for s in strs:
            l = [0] * 26
            for c in s:
                l[ord(c) - ord('a')] += 1
            d[tuple(l)].append(s)

        return list(d.values())