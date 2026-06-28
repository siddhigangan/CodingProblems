# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Handle empty lists edge case
        if not headA or not headB:
            return None
            
        temp1 = headA
        temp2 = headB
        
        # Loop continues until pointers either meet or both become None
        while temp1 != temp2:
            # If pointer reaches the end, redirect it to the other list's head
            temp1 = temp1.next if temp1 else headB
            temp2 = temp2.next if temp2 else headA
            
        # Returns either the intersection node or None
        return temp1
