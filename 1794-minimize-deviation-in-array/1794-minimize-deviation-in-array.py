class Solution:
    def minimumDeviation(self, nums):
        heap = []
        for num in nums:
            tmp = num
            while tmp%2 == 0: tmp//=2
            heap.append((tmp, max(num, tmp*2)))
        
        Max = max(i for i,j in heap)
        heapify(heap)
        ans = float("inf")

        while len(heap) == len(nums):
            num, limit = heappop(heap)
            ans = min(ans, Max - num)
            if num < limit:
                heappush(heap, (num*2, limit))
                Max = max(Max, num*2)
            
        return ans