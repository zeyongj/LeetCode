class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        
        # Use self. to call the method within the class
        return self.getMax(nums, 0, size - 1)
    
    def getMax(self, nums: List[int], left: int, right: int) -> int:
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2
        
        leftMax = self.getMax(nums, left, mid)
        rightMax = self.getMax(nums, mid + 1, right)
        middleMax = self.getMidMax(nums, left, mid, right)
        
        return max(leftMax, rightMax, middleMax)
    
    def getMidMax(self, nums: List[int], left: int, mid: int, right: int) -> int:
        if left == right:
            return nums[left]
        
        leftSum = 0
        leftMax = float('-inf')
        
        for i in range(mid, left - 1, -1):
            leftSum += nums[i]
            leftMax = max(leftMax, leftSum)
            
        rightSum = 0
        rightMax = float('-inf')
        
        for i in range(mid + 1, right + 1):
            rightSum += nums[i]
            rightMax = max(rightMax, rightSum)
        
        # Include nums[mid] in the sum across the middle
        return leftMax + rightMax

