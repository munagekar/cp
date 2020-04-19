"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List

"""
Another idea would be to do a bfs appending each level at a time.
Will be faster as well as dictionary lookup will be avoided.
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        l = [(root, 0)]

        if not root:
            return []

        ans = {}
        maxi = 0

        while l:
            node, level = l.pop(0)
            maxi = max(maxi, level)

            try:
                ans[level].append(node.val)
            except KeyError:
                ans[level] = [node.val]

            children = node.children
            for child in children:
                l.append((child, level + 1))

        return [ans[i] for i in range(maxi + 1)]