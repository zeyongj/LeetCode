class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = 0
        size = len(nums)
        for i in range(0, size):
            if (nums[i] != 0):
                nums[cur] = nums[i]
                cur += 1
        for i in range(cur, size):
            nums[i] = 0
