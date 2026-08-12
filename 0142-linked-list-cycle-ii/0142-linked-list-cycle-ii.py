class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        flag = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                flag = True
                break

        if flag == False:
            return None

        temp = head

        while temp != slow:
            temp = temp.next
            slow = slow.next

        return slow