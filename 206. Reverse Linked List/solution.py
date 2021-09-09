# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cursor = head

        while cursor:
            temp = cursor.next
            cursor.next = prev
            prev = cursor
            cursor = temp
    
        return prev
