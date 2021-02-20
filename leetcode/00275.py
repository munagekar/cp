# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        if not root:
            return []

        def explore(n, path):
            path.append(str(n.val))
            if not n.left and not n.right:
                path = "->".join(path)
                ans.append(path)
                return

            if n.left:
                explore(n.left, copy    .deepcopy(path))

            if n.right:
                explore(n.right, copy.deepcopy(path))

        explore(root, [])
        return ans