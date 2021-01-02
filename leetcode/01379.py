# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def solve(o, c, t):
            if not o:
                return None

            if o == t:
                return c

            return solve(o.left, c.left, t) or solve(o.right, c.right, t)

        return solve(original, cloned, target)