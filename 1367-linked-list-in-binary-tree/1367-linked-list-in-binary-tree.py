# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head, root):
        return self.dfs(head, head, root)

    def dfs(self, head, cur, root):
        if cur is None:  # Successfully matched the list
            return True
        if root is None:  # Reached the end of the tree without matching
            return False
        
        if cur.val == root.val:
            cur = cur.next  # Move to the next list node if value matches
        elif head.val == root.val:
            head = head.next  # Start new matching attempt if the value matches head of list
        else:
            cur = head  # Reset the matching pointer

        # Recursively check left and right subtrees
        return self.dfs(head, cur, root.left) or self.dfs(head, cur, root.right)