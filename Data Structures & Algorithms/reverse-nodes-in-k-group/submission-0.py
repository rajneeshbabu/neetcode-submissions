# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
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
        return curr
        