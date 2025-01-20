# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')

        def max_gain(node):
            if not node:
                return 0

            # Maximum gain from left and right subtrees
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # Price of the new path
            price_new_path = node.val + left_gain + right_gain

            # Update global max_sum if the new path is better
            self.max_sum = max(self.max_sum, price_new_path)

            # Return the max gain if the path continues through the parent
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_sum