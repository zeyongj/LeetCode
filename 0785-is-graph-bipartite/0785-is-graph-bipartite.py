from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        def dfs(node: int, c: int) -> bool:
            color[node] = c
            for nei in graph[node]:
                if color[nei] == -1:
                    if not dfs(nei, 1 - c):
                        return False
                elif color[nei] == color[node]:
                    return False
            return True
        
        for i in range(n):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        return True