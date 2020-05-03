class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        opts = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        if not digits:
            return []

        ans = ['']

        for digit in digits:
            opt = opts[int(digit)]
            lopt = len(opt)

            new_ans = []

            for char in opt:
                temp = [x + char for x in ans]
                new_ans.extend(temp)

            ans = new_ans

        return ans