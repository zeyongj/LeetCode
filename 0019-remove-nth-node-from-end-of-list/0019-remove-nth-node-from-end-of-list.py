# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        # Move first pointer n nodes ahead in the linked list
        for i in range(n + 1):
            first = first.next

        # Move first to the end, maintaining the gap
        while first is not None:
            first = first.next
            second = second.next

        # Skip the desired node
        second.next = second.next.next

        # Return the new head node
        return dummy.next