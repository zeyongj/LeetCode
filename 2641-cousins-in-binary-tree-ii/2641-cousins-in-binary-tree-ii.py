# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = collections.deque([root])
        root.val = 0
        while q:
            n, levelSum = len(q), 0
            for node in q:
                levelSum += (0 if not node.left else node.left.val) + (0 if not node.right else node.right.val)
            while n:
                node = q.popleft()
                val = levelSum - (0 if not node.left else node.left.val) - (0 if not node.right else node.right.val)
                if node.left:
                    node.left.val = val
                    q.append(node.left)
                if node.right:
                    node.right.val = val
                    q.append(node.right)
                n -= 1
        return root 