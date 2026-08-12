class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        # Find length of list A
        tempA = headA
        lenA = 0

        while tempA:
            lenA += 1
            tempA = tempA.next

        # Find length of list B
        tempB = headB
        lenB = 0

        while tempB:
            lenB += 1
            tempB = tempB.next

        # Reset pointers
        tempA = headA
        tempB = headB

        # Move the longer list forward
        if lenA > lenB:
            steps = lenA - lenB

            for _ in range(steps):
                tempA = tempA.next

        else:
            steps = lenB - lenA

            for _ in range(steps):
                tempB = tempB.next

        # Move both together
        while tempA != tempB:
            tempA = tempA.next
            tempB = tempB.next

        return tempA