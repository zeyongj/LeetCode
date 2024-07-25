class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 1
        temp = 1
        prev = nums[0]
        for num in nums:
            if num > prev:
                temp += 1
            else:
                if temp > res:
                    res = temp
                temp = 1
            prev = num
        return max(res, temp)