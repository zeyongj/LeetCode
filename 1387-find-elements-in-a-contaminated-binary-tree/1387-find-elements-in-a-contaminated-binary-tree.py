# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root):
        self.recoveredValues = set()
        root.val = 0
        self.recoverTree(root)

    def recoverTree(self, root):
        if not root:
            return
        self.recoveredValues.add(root.val)
        if root.left:
            root.left.val = 2 * root.val + 1
            self.recoverTree(root.left)
        if root.right:
            root.right.val = 2 * root.val + 2
            self.recoverTree(root.right)

    def find(self, target):
        return target in self.recoveredValues

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)