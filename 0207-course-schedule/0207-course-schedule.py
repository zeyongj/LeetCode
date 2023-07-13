from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
        
        visited = [0 for _ in range(numCourses)]
        
        def is_cyclic(i):
            if visited[i] == -1:  # cycle detected
                return True
            if visited[i] == 1:  # this node is already checked and is safe
                return False
            
            visited[i] = -1  # mark as being visited
            for j in graph[i]:
                if is_cyclic(j): 
                    return True
            visited[i] = 1  # mark as safe
            return False
        
        for i in range(numCourses):
            if is_cyclic(i):  # if a cycle is detected, return False
                return False
        return True
