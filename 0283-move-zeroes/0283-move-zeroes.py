class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        size = len(nums)
        
        index = 0
        
        for i in range(size):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
            else:
                continue
        
        while (index < size):
            nums[index] = 0
            index += 1
        