class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        h,w = len(grid), len(grid[0])

        # extract sequence and stripped
        top = [x for x in grid[0]]
        right = [row[-1] for row in grid[1:-1]]
        bottom = [x for x in grid[-1]][::-1]
        left = [row[0] for row in grid[1:-1]][::-1]
        sequence = top + right + bottom + left

        stripped = [[x for x in row[1:-1]] for row in grid[1:-1]]

        # rotate
        rotate = k%len(sequence)
        rearranged = sequence[rotate:] + sequence[:rotate]

        if stripped != [] and stripped[0] != []:
            stripped = self.rotateGrid(stripped, k)

        # reconstruct grid 
        top = rearranged[:w]
        right = rearranged[w:w+h-2]
        bottom = rearranged[w+h-2:w+h-2+w][::-1]
        left = rearranged[w+h-2+w:][::-1]

        grid = [[a] + b + [c] for a,b,c in zip(left, stripped, right)]
        grid = [top] + grid + [bottom]

        return grid