class Solution:
    def copyRandomList(self,head):
        if not head:
            return None
        
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next
        curr = head
        while curr:
            copy = curr.next
            if curr.random:
                copy.random = curr.random.next
            curr = copy.next
        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            if curr.next:
                copy.next = curr.next.next
            else:
                copy.next = None
            curr = curr.next
        return copy_head