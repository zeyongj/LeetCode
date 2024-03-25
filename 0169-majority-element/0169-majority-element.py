class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Divide and Conquer Method:
        return self.getMajority(nums, 0, len(nums)-1)
    def getMajority(self, nums, left, right) -> int:
        if left == right:
            return nums[left]
        
        mid = (left + right)//2
        
        leftMajor = self.getMajority(nums, left, mid)
        rightMajor = self.getMajority(nums, mid+1, right)
        
        if leftMajor == rightMajor:
            return leftMajor
        
        leftCount = 0
        rightCount = 0
        
        for i in range(left,right+1):
            if nums[i] == leftMajor:
                leftCount += 1
            elif nums[i] == rightMajor:
                rightCount += 1
        
        if leftCount > rightCount:
            return leftMajor
        else:
            return rightMajor
                    
        
#         HashMap Method:
#         num_map = {}
        
#         n = len(nums)
        
#         for num in nums:
#             if num not in num_map.keys():
#                 num_map[num] = 1
#             else:
#                 num_map[num] += 1
                
#         for key,value in num_map.items():
#             if value > n/2:
#                 return key