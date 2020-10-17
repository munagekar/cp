class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        h = jump = ListNode(next=head)

        l = r = head

        while True:
            count = 0
            while r and count < k:
                count += 1
                r = r.next

            if count != k:
                return h.next

            current = l
            previous = r
            for _ in range(k):
                tmp = current.next
                current.next = previous
                previous = current
                current = tmp

            jump.next = previous
            jump = l
            l = r