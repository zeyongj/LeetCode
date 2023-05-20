from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)
        results = []

        # Build the graph from equations
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0 / val

        # Perform each query via DFS
        for x, y in queries:
            results.append(self.dfs(x, y, graph, set()))

        return results

    def dfs(self, x, y, graph, visited):
        # If x is not in graph, no path
        if x not in graph:
            return -1.0

        # If we've reached the destination, return 1.0
        if x == y:
            return 1.0

        visited.add(x)

        for neighbor in graph[x]:
            if neighbor not in visited:
                val = self.dfs(neighbor, y, graph, visited)
                if val != -1.0:
                    return graph[x][neighbor] * val

        return -1.0
