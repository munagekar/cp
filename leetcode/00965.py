# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def search(node, val):
    if not node:
        return True

    if node.val != val:
        return False

    return search(node.left, val) and search(node.right, val)


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        return search(root, root.val)

