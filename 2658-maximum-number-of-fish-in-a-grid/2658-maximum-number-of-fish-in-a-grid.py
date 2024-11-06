class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fishes = 0

        def catchFish(r, c):
            nonlocal fish
            if 0 <= r < m and 0 <= c < n and grid[r][c] > 0:
                fish += grid[r][c]
                grid[r][c] = 0  # mark cell as visited
                catchFish(r+1, c)
                catchFish(r-1, c)
                catchFish(r, c+1)
                catchFish(r, c-1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    fish = 0
                    catchFish(r, c)
                    fishes = max(fishes, fish)

        return fishes