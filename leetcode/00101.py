# https://leetcode.com/problems/symmetric-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursive
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self._is_symetric(root.left, root.right)

    def _is_symetric(self, left, right) -> bool:
        if left is None or right is None:
            return left == right

        if left.val != right.val:
            return False

        return self._is_symetric(left.left, right.right) and self._is_symetric(left.right, right.left)


# Iterative
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        q = Queue()
        q.put(root.left)
        q.put(root.right)

        while not q.empty():
            left = q.get()
            right = q.get()

            if (left is None or right is None):
                if left != right:
                    return False
                else:
                    continue

            if left.val != right.val:
                return False

            q.put(left.left)
            q.put(right.right)
            q.put(left.right)
            q.put(right.left)

        return True
