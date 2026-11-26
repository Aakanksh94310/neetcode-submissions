class Solution:
    def reverseList(self,head):
        curr = head
        values = []

        while curr:
            values.append(curr.val)
            curr = curr.next
        new_head = None
        for val in values:
            node = ListNode(val)
            node.next = new_head
            new_head = node
        return new_head