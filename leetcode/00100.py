# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        def helper(a, b):
            if a is None or b is None:
                return a == b

            if a.val != b.val:
                return False

            return helper(a.left, b.left) and helper(a.right, b.right)

        return helper(p, q)