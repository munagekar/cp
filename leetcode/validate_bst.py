# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def populate(root, l):
            if not root:
                return
            populate(root.left, l)
            l.append(root.val)
            populate(root.right, l)

        l = list()
        populate(root, l)

        return all(i < j for i, j in zip(l, l[1:]))