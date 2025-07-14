# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans, curr=0, head
        while curr:
            ans=(ans<<1)+curr.val
            curr=curr.next
        return ans

        