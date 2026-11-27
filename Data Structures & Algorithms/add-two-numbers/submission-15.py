class Solution:
    def addTwoNumbers(self,l1,l2):

        def getNumber(head):
            number = 0
            place = 1
            while head:
                number += head.val * place
                place *= 10
                head = head.next
            return number
        total = getNumber(l1) + getNumber(l2)

        dummy = ListNode(0)
        curr = dummy

        if total == 0:
            return ListNode(0)

        while total > 0:
            digit = total % 10
            curr.next = ListNode(digit)
            curr = curr.next
            total = total // 10
        return dummy.next

        