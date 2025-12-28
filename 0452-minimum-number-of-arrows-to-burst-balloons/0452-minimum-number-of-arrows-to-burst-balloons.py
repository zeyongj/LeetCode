class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        pq = [(e, s) for s, e in points]   # store as (end, start)
        heapq.heapify(pq)

        arrows = 0
        last_end = -1

        while pq:
            end, start = heapq.heappop(pq)
            if last_end == -1:
                last_end = end
                arrows += 1
                continue

            if start > last_end:
                arrows += 1
                last_end = end

        return arrows