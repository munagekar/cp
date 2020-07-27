# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def solve(node, target, running_sum):
    if node.left is None and node.right is None:
        if target == node.val + running_sum:
            return True
        return False

    return (node.left != None and solve(node.left, target, running_sum + node.val)) or (
                node.right != None and solve(node.right, target, running_sum + node.val))


class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if root is None:
            return False
        return solve(root, target, 0)