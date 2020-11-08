# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def tilt(n):
    if n is None:
        return 0, 0

    l, ans1 = tilt(n.left)
    r, ans2 = tilt(n.right)
    ret = n.val + l + r
    n.val = abs(l - r)
    ans = n.val + ans1 + ans2
    return ret, ans


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        _, ans = tilt(root)
        return ans