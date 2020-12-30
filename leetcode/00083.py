# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head:
            return None

        p = head
        n = head.next

        while n:
            if n.val == p.val:
                n = n.next

            else:
                p.next = n
                p = n
                n = n.next

        p.next = None
        return head
