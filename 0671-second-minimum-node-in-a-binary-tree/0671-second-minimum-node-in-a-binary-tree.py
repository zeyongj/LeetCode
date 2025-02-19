# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findSecondMinimumValue(self, root):
        array=[]
        def traverse(node):
            if not node:
                return 
            array.append(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        array.sort()
        first_min=array[0]
        for i in range(1,len(array)):
            if array[i]>first_min:
                return array[i]
        return -1


        