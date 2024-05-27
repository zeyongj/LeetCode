class Solution:
    def get_first_greater_or_equal(self, nums, val):
        start = 0
        end = len(nums) - 1

        index = len(nums)
        while start <= end:
            mid = (start + end) // 2

            if nums[mid] >= val:
                index = mid
                end = mid - 1
            else:
                start = mid + 1

        return index
    
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        
        N = len(nums)
        for i in range(1, N + 1):
            k = self.get_first_greater_or_equal(nums, i)
            
            if N - k == i:
                return i
        
        return -1