class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        if (size == 0):
            return 0
        j = 0
        k = size  - 1
        while (j < k) :
            while (j < k and nums[j] != val):
                j += 1
            while (j < k and nums[k] == val):
                k -= 1
            temp = nums[j]
            nums[j] = nums[k]
            nums[k] = temp
        
        if (nums[j] == val):
            return j
        else:
            return (j+1)
