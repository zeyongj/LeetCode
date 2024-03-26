class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        
        return self.getMax(nums, 0, size - 1)
    
    def getMax(self, nums: List[int], left: int, right: int) -> int:
        size = len(nums)
        if left == right:
            return nums[left]
        
        mid = (left+right) // 2
        
        leftMax = self.getMax(nums, left, mid)
        rightMax = self.getMax(nums, mid+1, right)
        middleMax = self.getMidMax(nums, left, right)
        
        return max(leftMax, rightMax, middleMax)
    
    def getMidMax(self, nums: List[int], left: int, right: int) -> int:
        size = len(nums)
        mid = (left+right) // 2
        
        leftSum = nums[mid]
        leftMax = leftSum
        
        for i in range(mid-1, left-1, -1):
            leftSum += nums[i]
            leftMax = max(leftMax, leftSum)
            
        rightSum = nums[mid+1]
        rightMax = rightSum
        
        for i in range(mid+2, right+1):
            rightSum += nums[i]
            rightMax = max(rightMax, rightSum)
        
        middleMax = leftMax + rightMax
        return middleMax
            
        