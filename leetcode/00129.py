# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        if not root:
            return 0

        def solve(n, runner):

            runner = runner * 10 + n.val

            ans = 0

            if not n.left and not n.right:
                return runner

            if n.left:
                ans += solve(n.left, runner)
            if n.right:
                ans += solve(n.right, runner)

            return ans

        return solve(root, 0)
