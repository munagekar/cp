# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def solve(node: TreeNode):
    if node is None:
        return 0, 0

    lh, ld = solve(node.left)
    rh, rd = solve(node.right)
    return max(lh, rh) + 1, max(lh + rh, ld, rd)


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return solve(root)[1]