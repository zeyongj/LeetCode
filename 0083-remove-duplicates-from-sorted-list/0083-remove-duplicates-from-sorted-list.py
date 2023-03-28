# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = op = ListNode(0)
        while head.next:
            if head.val != head.next.val:
                op.next = head
                op = op.next
            head = head.next
        op.next = head
        return dummy.next