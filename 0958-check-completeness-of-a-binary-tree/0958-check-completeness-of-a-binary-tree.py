# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        missing = False
        while q:
            length = len(q)
            for _ in range(length):
                node = q.popleft()
                if node.left:
                    if missing:
                        return False            
                    q.append(node.left)
                else:
                    missing = True
                if node.right:
                    if missing:
                        return False
                    q.append(node.right)
                else:
                    missing = True
                    
        return True