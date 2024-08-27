import heapq
import math

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # Build the graph using an adjacency list
        graph = [[] for _ in range(n)]
        for (u, v), prob in zip(edges, succProb):
            log_prob = math.log(prob)
            graph[u].append((v, log_prob))
            graph[v].append((u, log_prob))
        
        # Max heap to prioritize higher log-probability paths
        heap = [(0.0, start)]  # Use 0.0 (log(1)) for the starting node
        
        # Track the minimum log-probability for each node
        log_dist = [float('inf')] * n
        log_dist[start] = 0.0
        
        # Dijkstra's algorithm with log-probabilities
        while heap:
            log_prob, node = heapq.heappop(heap)
            
            if node == end:
                return math.exp(-log_prob)  # Return the actual probability
            
            for neighbor, edge_log_prob in graph[node]:
                new_log_prob = log_prob - edge_log_prob  # log(x * y) = log(x) + log(y)
                
                if new_log_prob < log_dist[neighbor]:
                    log_dist[neighbor] = new_log_prob
                    heapq.heappush(heap, (new_log_prob, neighbor))
        
        return 0.0  # No path found