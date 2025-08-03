# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        from collections import defaultdict

        tree_map = defaultdict(int)
        duplicates = []

        def traverse(node):
            if not node:
                return "#"
            structure = "{},{},{}".format(node.val, traverse(node.left), traverse(node.right))
            tree_map[structure] += 1
            if tree_map[structure] == 2:
                duplicates.append(node)
            return structure

        traverse(root)
        return duplicates