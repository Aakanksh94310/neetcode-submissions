class Solution:
    def reorderList(self,head):
        if not head or not head.next:
            return
        
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        curr = second
        prev = None

        while curr:
            node_next = curr.next
            curr.next = prev
            prev = curr
            curr = node_next

        first = head 
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2



        