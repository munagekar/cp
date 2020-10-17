# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if not head:
            return

        prev = head
        n = head.next
        prev.next = None

        while n:
            tmp = n.next
            n.next = prev
            prev = n
            n = tmp

        return prev


class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        def helper(node):
            if node is None or node.next is None:
                return node

            tmp = helper(node.next)

            node.next.next = node
            node.next = None

            return tmp

        return helper(head)