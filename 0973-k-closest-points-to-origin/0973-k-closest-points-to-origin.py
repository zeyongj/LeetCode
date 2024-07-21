from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        size = len(points)
        
        dist = []
        for i in range(size):
            distance = points[i][0] * points[i][0] + points[i][1] * points[i][1]
            dist.append((distance, points[i]))
        
        dist.sort()
        
        ans = []
        for i in range(k):
            ans.append(dist[i][1])
        
        return ans
