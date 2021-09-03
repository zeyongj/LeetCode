class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        result = 0
        size = len(nums)
        if nums is None or size == 0:
            return 0
        # for i in range(0, size):
        #     if nums[i] == 1:
        #         count += 1
        #     else:
        #         result = max(result, count)
        #         count = 0
        for element in nums:
            if element == 1:
                count += 1
            else:
                result = max(result, count)
                count = 0
        # for index, element in enumerate(nums):
        #     if element == 1:
        #         count += 1
        #     else:
        #         result = max(result, count)
        #         count = 0
        return max(result, count)
