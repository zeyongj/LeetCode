class Solution(object):
    def validPath(self, n, edges, source, destination):
        
        # Create an adjacency list representation of the graph
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        # Function to perform depth-first search to find a path from source to destination
        def solve(graph, source, destination, visited):
            # If source and destination are the same, a path is found
            if source == destination:
                return True

            # Mark the current node as visited
            visited[source] = 1

            # Traverse through all adjacent vertices of the current vertex
            for neighbor in graph[source]:
                # If the neighbor is not visited, recursively search for a path
                if visited[neighbor] == 0:
                    if solve(graph, neighbor, destination, visited):
                        return True  # If a path is found, return true

            return False  # No path found from source to destination

        # Initialize a list to keep track of visited vertices
        visited = [0] * n

        # Call the helper function to find a path from source to destination
        return solve(graph, source, destination, visited)