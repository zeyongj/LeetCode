# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # make tuples of (depth, value) for each node in tree. reverse to pop starting from root
        nodes = [(len(node[1]), int(node[2])) for node in re.findall("((-*)(\d+))", traversal)][::-1]


        def makeTree(depth): 
            # tree build when nodes empty. if expected depth != current depth then reached leaf
            if not nodes or depth != nodes[-1][0]: return None 

            # preorder traversal = root - left - right
            node = TreeNode(nodes.pop()[1]) # pop node and get value
            node.left = makeTree(depth + 1) # fill in children at depth + 1. 
            node.right = makeTree(depth + 1)

            return node

        return makeTree(0) # start building tree, returns root