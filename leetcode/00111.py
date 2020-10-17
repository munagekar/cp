# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def mini(node, m, h):
    if h >= m:
        return m
    if node.left is None and node.right is None:
        return h

    if node.left:
        m = min(m, mini(node.left, m, h + 1))

    if node.right:
        m = min(m, mini(node.right, m, h + 1))

    return m


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return mini(root, math.inf, 1)