class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        # Construct the tree using the parent list.
        tree = defaultdict(list)
        for end,start in enumerate(parent):
            tree[start].append(end)
        
        # Store the longest path
        # It is updated in dfs
        res = 1
        
        # dfs will return the longest valid path starting from this node in the sub-tree rooted at this node.
        def dfs(node):
            nonlocal res
            
            # While examing the children, 
            # We want to keep track of the 2 longest paths starting from this node,
            # So that we can compute the longest path going through this node 
            # in the sub-tree rooted at this node.
            max1 = max2 = 0

            for nei in tree[node]:
                neiL = dfs(nei)
                # This condition makes sure the path is valid.
                if s[nei] != s[node]:
                    # Update the length of the top two longest paths.
                    if neiL > max1:
                        max2 = max1
                        max1 = neiL
                    elif neiL > max2:
                        max2 = neiL
            
            # Update the result.
            # Again, max1+max2+1 means the length of the longest valid path 
            # going through this node in the sub-tree rooted at this node.
            res = max(res, max1+max2+1)
            
            # Adding 1 for the current node
            return max1+1
        
        dfs(0)
        return res