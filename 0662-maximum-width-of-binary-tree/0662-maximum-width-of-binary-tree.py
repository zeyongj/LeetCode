# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root):
        level_old, num_old, max_width = 1, 1, 0
        queue = deque([[level_old,num_old,root]])

        while queue:    
            [num, level, node] = queue.popleft()
            if level > level_old:
                level_old, num_old = level, num
                
            max_width = max(max_width, num - num_old + 1)
            if node.left:  queue.append([num*2,  level+1, node.left])
            if node.right: queue.append([num*2+1,level+1, node.right])
                
        return max_width