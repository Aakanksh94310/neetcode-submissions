class Solution:
    def mergeTwoLists(self,list1,list2):
        dummy = ListNode(0)
        curr = dummy
        values = []

        while list1:
            values.append(list1.val)
            list1 = list1.next
        while list2:
            values.append(list2.val)
            list2 = list2.next
        values.sort()
        for val in values:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next
            