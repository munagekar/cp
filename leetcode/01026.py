# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        ans = 0

        def solve(n):
            nonlocal ans

            if not n.left and not n.right:
                return n.val, n.val

            mini = math.inf
            maxi = -math.inf
            if n.left:
                minil, maxil = solve(n.left)
                mini = min(mini, minil)
                maxi = max(maxi, maxil)
            if n.right:
                minir, maxir = solve(n.right)
                mini = min(mini, minir)
                maxi = max(maxi, maxir)

            ans = max(abs(mini - n.val), ans, abs(maxi - n.val))

            return min(mini, n.val), max(maxi, n.val)

        solve(root)
        return ans
