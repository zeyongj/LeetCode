# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.dfs(root, low, high)
        return self.sum 

    def dfs(self, root, low, high)-> None:
        if(root == None):
            return
        self.dfs(root.left, low, high)
        if(root.val <= high and root.val >= low):
            self.sum += root.val
        self.dfs(root.right, low, high)