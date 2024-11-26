# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #if there is no root node then return 0
        if not root:
            return 0
        #Make a function dfs to implement dfs
        def dfs(node, curMax):
        #If there is no node then terminate the recurssion
            if not node:
                return
        #if node value is greater then current value then increase count by 1 and update the max value
            if node.val >= curMax:
                count[0] += 1
                curMax = node.val
        #Specify dfs fuction so that it can go left and right in the tree
            dfs(node.left, curMax)
            dfs(node.right, curMax)
        #Make a variable count in which count will be store
        count = [0]
        #Call the fuction dfs
        dfs(root, root.val)
        #return count list as your answer
        return count[0]