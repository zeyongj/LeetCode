# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)            # Traverse left subtree
            dfs(node.right)           # Traverse right subtree
            result.append(node.val)   # Visit root
        
        dfs(root)
        return result