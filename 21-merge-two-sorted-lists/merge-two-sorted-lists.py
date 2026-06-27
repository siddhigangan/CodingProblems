class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a placeholder dummy node to build the new list
        dummy = ListNode()
        tail = dummy
        
        # 2. Loop while both lists have remaining elements
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # Move the tail pointer forward
            
        # 3. Append any remaining elements from either list
        tail.next = list1 if list1 else list2
        
        # 4. Return the actual starting node of the merged list
        return dummy.next
