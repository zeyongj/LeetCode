class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            heapq.heapify(row)

        res = 0
        while grid[0]:
            tmp = []
            for row in grid:
                tmp.append(heapq.heappop(row))
            res += max(tmp)

        return res