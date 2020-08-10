class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        levels = [0] * 1000

        def solve(node, l):
            if not node:
                return

            levels[l] += node.val

            solve(node.left, l + 1)
            solve(node.right, l + 1)

        solve(root, 0)
        return levels.index(max(levels)) + 1