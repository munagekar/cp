from collections import deque


class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens = sorted(tokens)
        tokens = deque(tokens)
        score = 0
        ans = 0

        while len(tokens) > 0:
            if P >= tokens[0]:
                P -= tokens[0]
                tokens.popleft()
                score += 1
                ans = max(score, ans)

            elif score > 0:
                P += tokens[-1]
                tokens.pop()
                score -= 1

            else:
                break

        return ans