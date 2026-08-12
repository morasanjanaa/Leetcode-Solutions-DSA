# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        temp = head
        while temp:
            size += 1
            temp = temp.next

        temp = head

        if size == 1:
            return None
        
        move = (size//2)

        for _ in range(move-1):
            temp = temp.next
        
        temp.next = temp.next.next

        return head

        