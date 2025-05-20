class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        for li, ri in queries:
            diff[li] -= 1
            if ri + 1 < n:
                diff[ri + 1] += 1
        sum_val = 0
        for i in range(n):
            sum_val += diff[i]
            if nums[i] > -sum_val:
                return False
        return True