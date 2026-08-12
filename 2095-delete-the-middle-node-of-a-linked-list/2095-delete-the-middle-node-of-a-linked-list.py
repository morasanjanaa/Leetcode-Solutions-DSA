# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        # Calculate the size for of LL
        size = 0
        temp = head
        while temp:
            size += 1
            temp = temp.next
        if size == 1:
            return None
        slow = head
        fast = head

        # Even Case
        if size % 2 == 0:
            while(fast.next.next != None):
                slow = slow.next
                fast = fast.next.next
        # Odd Case
        else:
            while(fast.next.next.next != None):
                slow = slow.next
                fast = fast.next.next

        slow.next = slow.next.next

        return head
        