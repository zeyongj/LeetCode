class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        x = []
        for i in range(len(nums)):
            if nums[i] == target:
                x.append(abs(i- start))
        return min(x)