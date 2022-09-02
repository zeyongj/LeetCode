# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        quene = []  
        res = []
        quene.append(root)
        while(quene):  
            qlen = len(quene)   
            tmp = 0
            for i in range(qlen):  
                node = quene.pop(0)
                tmp += node.val
                if node.left:   
                    quene.append(node.left)
                if node.right:
                    quene.append(node.right)
            res.append(tmp/qlen) 
        return res