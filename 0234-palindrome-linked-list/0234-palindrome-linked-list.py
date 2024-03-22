# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        numList = []
        
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy.next
        
        while (curr):
            numList.append(curr.val)
            curr = curr.next
        
        size = len(numList)
        left = 0
        right = size - 1
        
        while (left < right):
            if numList[left] != numList[right]:
                return False
            else:
                left += 1
                right -= 1
            
        return True
            
            