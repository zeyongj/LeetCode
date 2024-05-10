from heapq import heappush, heappop

class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        # Initialize the heap
        n = len(arr)
        heap = []
        for j in range(1, n):
            heappush(heap, (arr[0]/arr[j], 0, j))
        
        # Extract from the heap k times
        for _ in range(k):
            value, i, j = heappop(heap)
            if i + 1 < j:
                heappush(heap, (arr[i+1]/arr[j], i+1, j))
        
        return [arr[i], arr[j]]