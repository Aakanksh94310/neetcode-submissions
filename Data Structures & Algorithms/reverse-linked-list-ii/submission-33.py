class Solution:
    def reverseBetween(self,head,left,right):
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        i = left - 1
        j = right - 1
        while i < j:
            temp = values[i]
            values[i] = values[j]
            values[j] = temp
            i += 1
            j -= 1
        curr = head
        for val in values:
            curr.val = val
            curr = curr.next
        return head