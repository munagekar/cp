# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def solve(node, direction):
    if node.left is None and node.right is None:
        if direction == "l":
            return node.val
        return 0

    l = 0
    r = 0

    if node.left != None:
        l = solve(node.left, "l")

    if node.right != None:
        r = solve(node.right, "r")

    return l + r


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        return solve(root, "")
