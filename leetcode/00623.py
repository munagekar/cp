# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            return TreeNode(v, root)

        q = [root]

        while d > 2:
            d -= 1
            nq = []
            for n in q:
                if n.left:
                    nq.append(n.left)
                if n.right:
                    nq.append(n.right)
            q = nq

        for n in q:
            n.left = TreeNode(v, n.left)
            n.right = TreeNode(v, None, n.right)

        return root
