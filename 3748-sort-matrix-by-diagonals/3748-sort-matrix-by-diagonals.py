class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        import heapq
        n, m = len(grid), len(grid[0])
        diags = {}

        for i in range(n):
            for j in range(m):
                key = i - j
                if key not in diags: diags[key] = []
                if key < 0: heapq.heappush(diags[key], grid[i][j])
                else: heapq.heappush(diags[key], -grid[i][j])

        for i in range(n):
            for j in range(m):
                key = i - j
                if key < 0: grid[i][j] = heapq.heappop(diags[key])
                else: grid[i][j] = -heapq.heappop(diags[key])
        return grid