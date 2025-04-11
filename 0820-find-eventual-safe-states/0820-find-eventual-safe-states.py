class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''
        Track the nodes.
        0 - not visited
        1 - in process
        2 - fully processed
        '''
        visited = [0] * len(graph)
        def findCycle(index):
            #this node is confirmed not to be part of a cycle
            if visited[index] == 2:
                return False
            #found an in process node (cycle)
            if visited[index] == 1:
                return True

            #mark node as in progress and explore neighbors (DFS)
            visited[index] = 1
            for neighbor in graph[index]:
                if findCycle(neighbor):
                    return True

            #visited all neighbors and not found a cycle
            visited[index] = 2
            return False
  
        ans = []
        for i in range(len(graph)):
            if not findCycle(i):
                ans.append(i)
        return ans