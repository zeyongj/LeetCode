class Solution:
    def halveArray(self, nums):
        # Create a max-heap by using negative values
        pq = []
        totalOperations = 0
        sum_val = 0
        
        # Populate the heap and calculate the sum
        for num in nums:
            heapq.heappush(pq, -num)  # Use negative to simulate max-heap
            sum_val += num
        
        halveSum = sum_val / 2
        
        # Perform operations to halve the sum
        while sum_val > halveSum:
            totalOperations += 1
            num = -heapq.heappop(pq)  # Retrieve the largest element (negating back)
            sum_val -= num / 2
            heapq.heappush(pq, -(num / 2))  # Push the halved value back into the heap
        
        return totalOperations