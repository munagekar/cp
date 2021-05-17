# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:

        def solve(n, count):

            if n is None:
                return 0

            if n.left is None and n.right is None:
                return count * 2 + n.val

            return solve(n.left, count * 2 + n.val) + solve(n.right, count * 2 + n.val)

        return solve(root, 0)
