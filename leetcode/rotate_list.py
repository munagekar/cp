# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head

        p = head
        l = 1
        while p.next != None:
            p = p.next
            l += 1

        p.next = head

        r = k % l

        for _ in range(l - r):
            head = head.next

        new_head = head

        p = new_head
        for _ in range(l - 1):
            p = p.next

        p.next = None
        return new_head

