# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head):
        # Start with the first non-zero value.
        head = head.next
        if not head:
            return head

        # Initialize a dummy head node.
        temp = head
        sum = 0
        while temp.val != 0:
            sum += temp.val
            temp = temp.next

        # Store the sum in head's value.
        head.val = sum
        # Store head's next node as the recursive result for temp node.
        head.next = self.mergeNodes(temp)
        return head