# https://leetcode.com/problems/add-two-numbers/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
What do if the link list was reversed
1>Reverse Both List and use current solution
2>Use recursion to add equal sized lists
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = ListNode((l1.val + l2.val)%10 )
        ans = head  # Create a Copy to Return
        carry = (l1.val + l2.val) // 10
        l1 = l1.next
        l2 = l2.next
        while l1 and l2:
            head.next = ListNode((l1.val + l2.val + carry)%10)
            carry = (l1.val + l2.val + carry)//10
            head = head.next
            l1 = l1.next
            l2 = l2.next
        
        remain = None
        if l1:
            remain = l1
        
        if l2:
            remain = l2
        
        while remain:
            head.next = ListNode((remain.val + carry)%10)
            carry = (remain.val + carry) //10
            head = head.next
            remain = remain.next
            
        if carry:
            head.next = ListNode(1)
            
        return ans
            
        
        
        