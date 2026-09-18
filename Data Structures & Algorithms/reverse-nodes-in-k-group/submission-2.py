# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """if not head or k == 1:
            return head
        
        # Dummy node to easily handle head re-assignment
        dummy = ListNode(0)
        dummy.next = head
        
        # Pointers to track the boundary before the group
        group_prev = dummy
        
        while True:
            # Check if there are at least k nodes left in the current group
            kth = self.getKthNode(group_prev, k)
            if not kth:
                break
                
            # Track the start of the next group
            group_next = kth.next
            
            # Reverse the current k nodes
            prev = group_next
            current = group_prev.next
            
            while current != group_next:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
                
            # Connect the previous group to the new head of this reversed group
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
            
        return dummy.next
    
    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr"""
        if not head or k == 1:
            return head

        # 2. BUG FIX: Count if there are actually k nodes available to reverse
        check_curr = head
        for _ in range(k):
            if not check_curr:
                return head  # Fewer than k nodes left, return head as-is
            check_curr = check_curr.next

        # 3. Setup pointers for the reversal
        prev = None
        curr = head
        count = 0

        # 4. Reverse the current k nodes
        while curr is not None and count < k:
            next_node = curr.next  # Using 'next_node' to avoid Python keyword conflict
            curr.next = prev
            prev = curr
            curr = next_node
            count += 1

        # 5. BUG FIX: Recursively stitch the remaining groups
        # 'curr' now points to the start of the next group (what used to be 'next')
        if curr is not None:
            # 'head' is now the tail of our reversed segment.
            # We connect it to the result of the next recursive group.
            head.next = self.reverseKGroup(curr, k)

        # 6. 'prev' has become the new head of this reversed k-group segment
        return prev

        