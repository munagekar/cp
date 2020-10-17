class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        def helper(left, right):

            if left:
                left.left, left.right = helper(left.left, left.right)

            if right:
                right.left, right.right = helper(right.left, right.right)

            return right, left

        root.left, root.right = helper(root.left, root.right)

        return root