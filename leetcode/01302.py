# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


def solve(node, level, d):
    if node == None:
        return
    d[level] += node.val
    solve(node.left, level + 1, d)
    solve(node.right, level + 1, d)


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        d = defaultdict(lambda: 0)
        solve(root, 0, d)

        return max(d.items())[1]