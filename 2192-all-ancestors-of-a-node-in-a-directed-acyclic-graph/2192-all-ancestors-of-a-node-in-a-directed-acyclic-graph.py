class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res = [[] for _ in range(n)]
        graph = [[] for _ in range(n)]
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
        
        for i in range(n):
            self.dfs(graph, i, i, res, [False] * n)
        
        for i in range(n):
            res[i].sort()
        
        return res
    
    def dfs(self, graph, parent, curr, res, visit):
        visit[curr] = True
        for dest in graph[curr]:
            if not visit[dest]:
                res[dest].append(parent)
                self.dfs(graph, parent, dest, res, visit)        