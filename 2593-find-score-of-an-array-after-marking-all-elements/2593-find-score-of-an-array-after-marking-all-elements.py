class Solution(object):
    def findScore(self, nums):
        minHeap = []
        for i in range(len(nums)):
            heappush(minHeap, (nums[i],i))
        
        score = 0
        while len(minHeap) > 0:
            x = heappop(minHeap)
            if nums[x[1]] == 0:
                continue
            else:
                score += nums[x[1]]
                nums[x[1]] = 0
                if x[1] > 0:
                    nums[x[1] - 1] = 0
                if x[1] < len(nums) - 1:
                    nums[x[1] + 1] = 0
        return score