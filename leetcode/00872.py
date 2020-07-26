# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def leaf_seq(arr, node):
    if node.left != None:
        leaf_seq(arr, node.left)
    if node.right != None:
        leaf_seq(arr, node.right)

    if node.left == None and node.right == None:
        arr.append(node.val)


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        s1 = []
        s2 = []
        leaf_seq(s1, root1)
        leaf_seq(s2, root2)
        return s1 == s2