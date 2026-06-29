# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = head
        turtle = head

        while turtle and turtle.next :
            hare = hare.next
            turtle = turtle.next.next

            if turtle == hare :
                return True

        return False 
