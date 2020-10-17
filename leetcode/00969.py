def pancake(A, k):
    return A[k::-1] + A[k + 1:]


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        l = len(A)

        res = []

        for end in range(l - 1, 0, -1):
            maxi = max(itertools.islice(A, 0, end + 1))
            idx = A.index(maxi)
            if idx != end:
                A = pancake(A, idx)
                if idx != 0:
                    res.append(idx)
                A = pancake(A, end)
                res.append(end)
        return [1 + x for x in res]