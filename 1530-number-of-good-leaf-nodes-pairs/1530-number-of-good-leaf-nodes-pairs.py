# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        graph = collections.defaultdict(list)
        
        def dfs(node, par = None):
            if node:
                graph[node].append(par)
                graph[par].append(node)
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        
        leaves = []
        for node in graph.keys():
            if node and not node.left and not node.right:
                leaves.append(node)
        
        count = 0
        
        for leaf in leaves:
            queue = [(leaf,0)]
            seen = set(queue)
            while queue:
                node,length = queue.pop(0)
                if length>distance:
                    break
                if node:
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            queue.append((nei,length+1))
                    if node!=leaf and not node.left and not node.right and length<=distance:
                        count+=1
                    
        return count//2