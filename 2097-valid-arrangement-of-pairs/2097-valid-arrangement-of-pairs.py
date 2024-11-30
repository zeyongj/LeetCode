class Solution:
    def validArrangement(self, pairs):
        from collections import defaultdict, deque

        graph = defaultdict(deque)
        inDegree, outDegree = defaultdict(int), defaultdict(int)

        for start, end in pairs:
            graph[start].append(end)
            outDegree[start] += 1
            inDegree[end] += 1

        startNode = pairs[0][0]
        for node in graph:
            if outDegree[node] == inDegree[node] + 1:
                startNode = node
                break

        path = []

        def dfs(node):
            while graph[node]:
                nextNode = graph[node].popleft()
                dfs(nextNode)
            path.append(node)

        dfs(startNode)
        path.reverse()
        
        return [[path[i], path[i+1]] for i in range(len(path) - 1)]