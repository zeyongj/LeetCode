# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        result = self.heist(root)
        return max(result[0], result[1])

    def heist(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return [0, 0]

        leftSubtree = self.heist(root.left)

        rightSubtree = self.heist(root.right)

        includeRoot = root.val + leftSubtree[1] + rightSubtree[1]

        excludeRoot = max(leftSubtree[0], leftSubtree[1]) + max(
            rightSubtree[0], rightSubtree[1]
        )

        return [includeRoot, excludeRoot]