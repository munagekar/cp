class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:

        NO_COLOR = 0
        BLUE = 1
        GREEN = -1

        mapi = collections.defaultdict(list)
        cmap = [0] * N
        for i, j in dislikes:
            i = i - 1
            j = j - 1
            mapi[i].append(j)
            mapi[j].append(i)

        def helper(node, color):
            cmap[node] = color

            for n in mapi[node]:

                if cmap[n] == color:
                    return False

                elif cmap[n] == NO_COLOR and not helper(n, -color):
                    return False
            return True

        for i in range(N):
            if cmap[i] == NO_COLOR and not helper(i, BLUE):
                return False

        return True



