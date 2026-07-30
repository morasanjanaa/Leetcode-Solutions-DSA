# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        if count==1:
            head.next = None
            return
        mid = count//2
        temp = head
        while(mid>1):
            temp = temp.next
            mid -= 1
        temp.next = temp.next.next
        
        return head
    
    

        