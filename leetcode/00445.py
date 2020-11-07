# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def le(l):
    count = 0

    while l is not None:
        count += 1
        l = l.next

    return count


def z(l, c):
    s = ListNode(0)
    p = s
    while c > 1:
        p.next = ListNode(0)
        p = p.next
        c -= 1

    p.next = l

    return s


def add(a, b):
    if a is None:
        return 0, None

    c, n = add(a.next, b.next)

    c, s = divmod(a.val + b.val + c, 10)
    ans = ListNode(s)

    if n:
        ans.next = n

    return c, ans


def printl(l):
    vals = []
    while l:
        vals.append(l.val)
        l = l.next

    print(vals)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        len1 = le(l1)
        len2 = le(l2)

        if len1 > len2:
            l2 = z(l2, len1 - len2)
        elif len2 > len1:
            l1 = z(l1, len2 - len1)

        c, ans = add(l1, l2)

        if c:
            l = ListNode(1)
            l.next = ans
            return l

        return ans