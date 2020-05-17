"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None

        q = [head]

        while len(q) != 0:
            n = q.pop()
            if n.child:
                if n.next is not None:
                    q.append(n.next)
                n.next = n.child
                n.child.prev = n
                q.append(n.child)
                n.child = None

                continue
            if not n.next:
                try:
                    n.next = q[-1]
                    q[-1].prev = n
                except IndexError:
                    n.next = None
                continue
            q.append(n.next)
        return head

