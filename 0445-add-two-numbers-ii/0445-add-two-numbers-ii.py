# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Helper function to reverse a linked list
    def reverseLL(self, head):
        if not head or not head.next:
            return head  # Base case: If the list is empty or has one node, return as is
        
        last = self.reverseLL(head.next)  # Recursive call to reverse the rest of the list
        head.next.next = head  # Reverse the current node
        head.next = None  # Set the next pointer to None to avoid cycles
        return last  # Return the new head of the reversed list

    def addTwoNumbers(self, l1, l2):
        # Step 1: Reverse both input linked lists
        l1 = self.reverseLL(l1)
        l2 = self.reverseLL(l2)

        sum_val = 0
        carry = 0
        
        # Dummy node to simplify result list construction
        ans = ListNode(0)

        # Step 2: Traverse both lists and calculate the sum
        while l1 or l2:
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next

            # Step 3: Store the current digit and update the carry
            ans.val = sum_val % 10
            carry = sum_val // 10

            # Step 4: Create a new node for the next digit and insert it at the front
            new_node = ListNode(carry)
            new_node.next = ans
            ans = new_node

            # Reset sum to carry for the next iteration
            sum_val = carry

        # Step 5: Return the correct head (skip leading zero if no carry remains)
        return ans.next if carry == 0 else ans