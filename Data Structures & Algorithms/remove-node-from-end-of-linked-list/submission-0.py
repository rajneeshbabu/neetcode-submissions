# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next

        
        steps_to_target = l - n
        curr = dummy
        
        for _ in range(steps_to_target):
            curr = curr.next
            
        # 4. Skip the N-th node from the end
        curr.next = curr.next.next
        
        # 5. Return the true head of the list
        return dummy.next




        