class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        heap = [[0,grid[0][0],0,0]] #cost, flag, r, c
        directions = [[], [0, 1], [0, -1], [1, 0], [-1, 0]] # start at index 1
        visit = set()
        while heap:
            d, f, r, c = heapq.heappop(heap)
            if r == rows - 1 and c == cols -1:
                return d
            if min(r,c) < 0 or r == rows or c == cols or (r,c) in visit:
                continue
            visit.add((r,c))
            
            for i in range(1, 5):
                cost = 1
                dr, dc = directions[i]
                newR, newC = dr + r, c + dc
                if min(newR, newC) < 0 or newR == rows or newC == cols or (newR, newC) in visit:
                    continue
                
                if i == f:
                    cost = 0
                heapq.heappush(heap, [d + cost, grid[newR][newC], newR, newC])
