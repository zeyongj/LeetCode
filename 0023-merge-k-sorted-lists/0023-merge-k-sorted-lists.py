# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists):
        pq = PriorityQueue()

        for i, head in enumerate(lists):
            if head:
                pq.put((head.val, i, head))

        dummy = ListNode()
        tail = dummy

        while not pq.empty():
            _, i, node = pq.get()

            tail.next = node
            tail = tail.next

            if node.next:
                pq.put((node.next.val, i, node.next))

        return dummy.next