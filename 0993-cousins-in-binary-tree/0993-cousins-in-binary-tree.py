# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        levelFound = -1
        ans = False
        foundRoot = -1
        def helper(curr = root, level = 0, par = 0):
            nonlocal levelFound, ans, foundRoot
            if curr:
                if curr.val == x or curr.val == y:
                    if levelFound + 1 and foundRoot + 1:
                        ans = levelFound == level and foundRoot != par
                        return
                    else:
                        levelFound = level
                        foundRoot = par
                helper(curr.left, level + 1, curr.val)
                helper(curr.right, level + 1, curr.val)
            return
        helper()
        return ans