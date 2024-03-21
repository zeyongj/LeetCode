# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ListNode(0)  # Create a dummy head to simplify edge cases
        dummy.next = head
        prev, curr = dummy, head
        
        while (curr != None):
            if (curr.val != val):
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                curr = curr.next
        
        return dummy.next
            
        
        