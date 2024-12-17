class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        maxSum = sum([max(0, num) for num in nums])
        absNums = sorted([abs(num) for num in nums])
        maxHeap, nextSum = [(-maxSum + absNums[0], 0)], -maxSum
        for _ in range(k - 1):
            nextSum, i = heapq.heappop(maxHeap)
            if i + 1 < len(absNums):
                heapq.heappush(maxHeap, (nextSum - absNums[i] + absNums[i + 1], i + 1))
                heapq.heappush(maxHeap, (nextSum + absNums[i + 1], i + 1))
        return -nextSum