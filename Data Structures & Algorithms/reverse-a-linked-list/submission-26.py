class Solution:
    def reverseList(self,head):
        prev = None
        curr = head

        while curr:
            node_next = curr.next
            curr.next = prev
            prev = curr
            curr = node_next
        return prev