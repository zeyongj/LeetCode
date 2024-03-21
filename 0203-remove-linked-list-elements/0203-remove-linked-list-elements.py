# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ListNode(0,None)
        dummy.next = head
        prev = dummy
        
        while (head != None):
            if (head.val is not val):
                prev = head
                head = head.next
            else:
                prev.next = head.next
                head = head.next
        
        return dummy.next
            
        
        