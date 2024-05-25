from typing import List
import math

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        def count_darts_in_circle(cx, cy):
            count = 0
            r_squared = r * r
            for x, y in darts:
                if (x - cx) ** 2 + (y - cy) ** 2 <= r_squared + 1e-7:  # Adjust for floating-point precision
                    count += 1
            return count

        n = len(darts)
        if n == 1:
            return 1

        max_darts = 1
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = darts[i]
                x2, y2 = darts[j]
                # Distance between points i and j
                dist_ij = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                
                if dist_ij > 2 * r:
                    continue  # Cannot form a valid circle that includes both points
                
                # Midpoint between points
                mid_x = (x1 + x2) / 2
                mid_y = (y1 + y2) / 2
                
                # Distance from midpoint to the center of circle
                dist_to_center = math.sqrt(r * r - (dist_ij / 2) ** 2)
                
                # Direction to move from midpoint to center (perpendicular to line AB)
                angle = math.atan2(y2 - y1, x2 - x1) + math.pi / 2
                
                # Two possible centers
                centers = [
                    (mid_x + dist_to_center * math.cos(angle), mid_y + dist_to_center * math.sin(angle)),
                    (mid_x - dist_to_center * math.cos(angle), mid_y - dist_to_center * math.sin(angle))
                ]
                
                for cx, cy in centers:
                    max_darts = max(max_darts, count_darts_in_circle(cx, cy))
        
        return max_darts
