# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        def solve(node):
            if not node:
                return None
            
            if not node.next:
                return node
        
            f = node
            s = node.next
            t = s.next
            
            s.next = f
            f.next = solve(t)
            return s
        
        return solve(head)
            
