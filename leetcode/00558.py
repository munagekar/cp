"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':

        def solve(n1, n2):
            if n1.isLeaf:
                return n1 if n1.val else n2

            if n2.isLeaf:
                return n2 if n2.val else n1

            topleft = solve(n1.topLeft, n2.topLeft)
            topright = solve(n1.topRight, n2.topRight)
            bottomleft = solve(n1.bottomLeft, n2.bottomLeft)
            bottomright = solve(n1.bottomRight, n2.bottomRight)

            if topleft.val == topright.val and topright.val == bottomleft.val and bottomright.val == bottomleft.val and topleft.isLeaf and topright.isLeaf and bottomleft.isLeaf and bottomright.isLeaf:
                return Node(topleft.val, True, None, None, None, None)

            return Node(False, False, topleft, topright, bottomleft, bottomright)

        return solve(quadTree1, quadTree2)



