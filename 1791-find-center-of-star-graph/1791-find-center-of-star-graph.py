class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        mapping = {}
        n = 0
        
        for edge in edges:
            for vertex in edge:
                if vertex > n:
                    n = vertex
                    
                if vertex not in mapping:
                    mapping[vertex] = 1
                else:
                    mapping[vertex] += 1
        
        
        for vertex, degree in mapping.items():
            if degree == n - 1:
                return vertex
        
        return -1