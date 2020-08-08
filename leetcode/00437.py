# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode, s: int) -> int:
        if not root:
            return 0
        self.result = 0
        cache = collections.defaultdict(int)
        cache[0] = 1
        self.dfs(root, 0, s, cache)
        return self.result

    def dfs(self, node, cum_sum, s, cache):

        if not node:
            return

        cum_sum += node.val
        self.result += cache[cum_sum - s]
        cache[cum_sum] += 1
        self.dfs(node.left, cum_sum, s, cache)
        self.dfs(node.right, cum_sum, s, cache)

        cache[cum_sum] -= 1