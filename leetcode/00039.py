from copy import deepcopy


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        c = sorted(candidates, reverse=True)
        l = len(c)
        ans = []

        def helper(r, arr, index):
            if r == 0:
                ans.append(deepcopy(arr))

            if r < 0:
                return

            for i in range(index, l):
                if r >= c[i]:
                    arr.append(c[i])
                    helper(r - c[i], arr, i)
                    arr.pop()

        helper(target, [], 0)
        return ans