# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val \U0001f921
#         self.left = left \U0001f921
#         self.right = right \U0001f921
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        cur = -1
        state = True
        def dfs(node) :
            nonlocal state, cur
            if not node :
                return 
            if not (cur == -1 or node.val == cur) :
                state = False
            cur = node.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return state