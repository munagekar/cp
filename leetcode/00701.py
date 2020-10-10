# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def helper(root, val):
    if val > root.val:
        if root.right is not None:
            helper(root.right, val)
        else:
            root.right = TreeNode(val)
    else:
        if root.left is not None:
            helper(root.left, val)
        else:
            root.left = TreeNode(val)


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        helper(root, val)
        return root