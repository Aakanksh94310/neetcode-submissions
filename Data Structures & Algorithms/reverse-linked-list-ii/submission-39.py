class Solution:
    def reverseBetween(self,head,left,right):
        dummy = ListNode(0)
        dummy.next = head
        before = dummy

        for _ in range(left-1):
            before = before.next
        curr = before.next
        tail = curr
        prev = None
        for _ in range(right-left+1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        before.next = prev
        tail.next = curr
        return dummy.next