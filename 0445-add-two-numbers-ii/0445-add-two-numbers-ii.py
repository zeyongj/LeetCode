# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        
        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        sum = 0
        result = ListNode(0)
        while s1 or s2:
            if s1:
                sum += s1.pop()
            if s2:
                sum += s2.pop()
            result.val = sum % 10
            head = ListNode(sum // 10)
            head.next = result
            result = head
            sum //= 10
            
        return result.next if result.val == 0 else result
