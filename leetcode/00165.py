class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))

        l = max(len(v1), len(v2))

        v1 = v1 + (l - len(v1)) * [0]
        v2 = v2 + (l - len(v2)) * [0]

        for x, y in zip(v1, v2):
            if x > y:
                return 1
            elif x < y:
                return -1

        return 0