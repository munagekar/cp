class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        last_char = "*"
        count = 0

        for c in s:
            if c != last_char:
                last_char = c
                stack.append((c, 1))
                count = 1

            elif c == last_char:
                count += 1
                if count != k:
                    stack.append((c, count))

                else:
                    for _ in range(k - 1):
                        stack.pop()
                    if stack:
                        last_char, count = stack[-1]

        return "".join(s[0] for s in stack)
