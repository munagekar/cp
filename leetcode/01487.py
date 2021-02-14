class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:

        out = set()
        outl = list()
        counter = collections.defaultdict(lambda: 1)
        for n in names:
            if n not in out:
                out.add(n)
                outl.append(n)
                continue

            i = counter[n]
            while f"{n}({i})" in out:
                i += 1
            out.add(f"{n}({i})")
            outl.append(f"{n}({i})")
            counter[n] = i + 1

        return outl