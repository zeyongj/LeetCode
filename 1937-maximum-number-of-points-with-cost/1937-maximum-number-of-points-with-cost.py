class Solution:
    def maxPoints(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        current = [0] * width
        previous = [0] * width
        
        for level in grid:
            peak = 0
            # Forward sweep
            for i in range(width):
                peak = max(peak - 1, previous[i])
                current[i] = peak
            
            peak = 0
            # Backward sweep
            for i in range(width - 1, -1, -1):
                peak = max(peak - 1, previous[i])
                current[i] = max(current[i], peak) + level[i]
            
            previous, current = current, previous
        
        return max(previous)