# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        s = deque()
        s.append((root, 0))

        ans = []

        if not root:
            return []

        while s:
            n, l = s.popleft()
            try:
                ans[l] = n.val
            except:
                ans.append(n.val)

            if n.left:
                s.append((n.left, l + 1))

            if n.right:
                s.append((n.right, l + 1))

        return ans