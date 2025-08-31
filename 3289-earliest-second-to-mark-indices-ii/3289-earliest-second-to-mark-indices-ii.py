class Solution:
    def earliestSecondToMarkIndices(self, A: List[int], B: List[int]) -> int:
        firsts = {}
        for i, b in enumerate(B):
            if A[b - 1] and b not in firsts:
                firsts[b] = i
        
        firsts_inv = {i: b for b, i in firsts.items()}

        def possible(bound):
            # Is B[:bound] enough to clear A?
            pq = []
            mark = 0

            for i in range(bound - 1, -1, -1):
                if i in firsts_inv:
                    heappush(pq, A[firsts_inv[i] - 1])
                    
                    if mark:
                        mark -= 1
                    else:
                        mark += 1
                        heappop(pq)
                else:
                    mark += 1

            return sum(A) - sum(pq) + len(A) - len(pq) <= mark

        lo, hi = 0, len(B) + 1
        while lo < hi:
            mi = lo + hi >> 1
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi
        
        return lo if lo <= len(B) else -1