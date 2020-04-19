class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_indices = {c: i for i, c in enumerate(s)}

        ans = []
        done = set()
        for i, c in enumerate(s):
            if c in done:
                continue
            while ans and ans[-1] > c and last_indices[ans[-1]] > i:
                done.remove(ans.pop())
            ans.append(c)
            done.add(c)

        return "".join(ans)
