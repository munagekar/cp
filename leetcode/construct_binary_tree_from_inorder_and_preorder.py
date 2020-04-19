# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def bt(preord, inord, start, end):
    global counter
    if start > end:
        return None

    val = preord.pop(0)
    root = TreeNode(val)
    ri = inord.index(val)
    root.left = bt(preord, inord, start, ri - 1)
    root.right = bt(preord, inord, ri + 1, end)

    return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return bt(preorder, inorder, 0, len(preorder) - 1)