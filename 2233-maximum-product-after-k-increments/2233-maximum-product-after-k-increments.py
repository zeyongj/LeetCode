class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        while k:
            k -= 1

            # Increment the current least value in the heap until k operations are done
            min_heap = heapq.heappop(nums) + 1
            heapq.heappush(nums, min_heap)

        return self.calcProduct(nums)
    
    def calcProduct(self, nums):
        product = 1
        for num in nums:
            product = (product * num) % 1000000007
        return product