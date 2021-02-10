class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        n = head
        m = head

        d = dict()
        d[None] = None

        while n:
            d[n] = Node(n.val)
            n = n.next

        while m:
            d[m].random = d[m.random]
            d[m].next = d[m.next]
            m = m.next

        return d[head]


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution2:
    def copyRandomList(self, head: 'Node') -> 'Node':
        n = head
        d = collections.defaultdict(lambda: Node(0))
        d[None] = None
        while n:
            d[n].val = n.val
            d[n].random = d[n.random]
            d[n].next = d[n.next]
            n = n.next

        return d[head]