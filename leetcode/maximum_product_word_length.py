import string
import itertools


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mapi = {}
        for bit, char in enumerate(string.ascii_lowercase):
            mapi[char] = 2 ** bit

        masks = []
        for word in words:
            mask = 0
            for char in word:
                mask = mask | mapi[char]
            masks.append((mask, len(word)))

        ans = 0
        for mask1, mask2 in itertools.combinations(masks, 2):
            if not mask1[0] & mask2[0]:
                ans = max(mask1[1] * mask2[1], ans)

        return ans