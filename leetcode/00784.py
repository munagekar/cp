class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        s = S.lower()
        ans = [""]
        for c in s:
            if c.isalpha():
                ans = ans + copy.deepcopy(ans)
                for i in range(len(ans) // 2):
                    ans[i] += c
                c = c.upper()

                for i in range(len(ans) // 2, len(ans)):
                    ans[i] += c
            else:
                ans = [x + c for x in ans]
        return ans