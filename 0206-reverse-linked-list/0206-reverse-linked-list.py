# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        res = self.reverseList(head.next)
        
        head.next.next = head
        head.next = None
        
        return res
        
        
#         prev = None
#         curr = head
        
#         while (curr != None):
#             curr_next = curr.next
#             curr.next = prev
#             prev = curr
#             curr = curr_next
        
#         return prev