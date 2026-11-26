class Solution:
    def copyRandomList(self,head):
        copies = {}
        curr = head
        while curr:
            copies[curr] = Node(curr.val)
            curr = curr.next
        copies[None] = None
        curr = head
        while curr:
            copies[curr].next = copies[curr.next]
            copies[curr].random = copies[curr.random]
            curr = curr.next
        return copies[head]