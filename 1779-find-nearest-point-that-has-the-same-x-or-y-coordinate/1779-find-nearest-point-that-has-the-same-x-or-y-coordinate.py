import math

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        size = len(points)
        
        ans= [-1] * size

        for i in range(size):
            if points[i][0] == x or points[i][1] == y:
                ans[i] = abs(points[i][0] - x) + abs(points[i][1] - y)
        
        smallest_distance = math.inf
        
        for dis in ans:
            if dis < smallest_distance and dis >= 0:
                smallest_distance = dis
        
        if smallest_distance == math.inf:
            return -1
        
        for i in range(size + 1):
            if ans[i] == smallest_distance:
                return i