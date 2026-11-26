class Solution:
    def reverseList(self,head):
        curr = head
        prev = None
        while curr:
            node_next = curr.next
            curr.next = prev
            prev = curr
            curr = node_next
        return prev