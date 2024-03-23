import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = len(nums)
        
        temp = [-1 * num for num in nums]
        heapq.heapify(temp)
        output = 0
        
        if k < size:
            for i in range(k):
                output = heapq.heappop(temp)
        else:
            for i in range(size):
                output = heapq.heappop(temp)
        
        return -1*output
        