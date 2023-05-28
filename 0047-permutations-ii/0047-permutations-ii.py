class Solution:
    def permuteUnique(self, nums):
        def backtrack(start, end):
            if start == end:
                result.append(nums[:])
            for i in range(start, end):
                if nums[i] in nums[start:i]:  # skip duplicates
                    continue
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1, end)
                nums[start], nums[i] = nums[i], nums[start]  # undo the swap

        nums.sort()
        result = []
        backtrack(0, len(nums))
        return result
