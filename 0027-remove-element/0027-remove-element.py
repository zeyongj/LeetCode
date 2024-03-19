class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        k = 0
        
        for i in range(size):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k