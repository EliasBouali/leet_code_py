# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry :
            if l1 :
                valueL1 = l1.val
            else :
                valueL1 = 0

            if l2 :
                valueL2 = l2.val
            else :
                valueL2 = 0

            total = valueL1 + valueL2 + carry

            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next
            if l1 :
                l1 = l1.next
            if l2 :
                l2 = l2.next

        return dummy.next
