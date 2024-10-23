class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [0] * (n + 1)
        uf_parent = [i for i in range(n + 1)]
        
        candidate1 = None  # First edge causing a node to have two parents
        candidate2 = None  # Second edge causing a node to have two parents
        
        # Function to find the root of a node
        def find(u):
            while uf_parent[u] != u:
                uf_parent[u] = uf_parent[uf_parent[u]]  # Path compression
                u = uf_parent[u]
            return u
        
        # First pass: detect a node with two parents
        for u, v in edges:
            if parent[v] == 0:
                parent[v] = u
            else:
                # Node v has two parents
                candidate1 = [parent[v], v]
                candidate2 = [u, v]
                # Temporarily remove candidate2 from the edges
                break
        
        # Initialize Union-Find parent array
        uf_parent = [i for i in range(n + 1)]
        
        # Second pass: Union-Find to detect cycles
        for u, v in edges:
            # Skip candidate2 if it exists
            if candidate2 and [u, v] == candidate2:
                continue
            pu = find(u)
            pv = find(v)
            if pu == pv:
                # Cycle detected
                if candidate1:
                    # If there's a node with two parents, return candidate1
                    return candidate1
                else:
                    # No node with two parents, return the current edge
                    return [u, v]
            uf_parent[pv] = pu  # Union operation
        
        # If no cycles detected, return candidate2
        return candidate2
