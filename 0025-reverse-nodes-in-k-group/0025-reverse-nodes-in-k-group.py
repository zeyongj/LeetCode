# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        tail = dummy

        length = 0
        while curr:
            length += 1
            curr = curr.next

        while length >= k:
            curr = prev.next
            tail = prev
            for _ in range(k):
                tail = tail.next
            next_group_start = tail.next
            tail.next = None

            prev.next = self.reverse_list(curr)
            curr.next = next_group_start
            prev = curr

            length -= k

        return dummy.next

    def reverse_list(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
