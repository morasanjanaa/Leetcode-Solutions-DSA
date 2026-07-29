# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        size = 0

        while temp:
            size += 1
            temp = temp.next

        mid = size // 2

        temp = head
        
        while mid:
            temp = temp.next
            mid -= 1

        return temp


        

    

        