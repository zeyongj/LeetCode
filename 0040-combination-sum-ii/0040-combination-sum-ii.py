class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        self._combine(candidates, 0, [], target, result)
        return result

    def _combine(self, nums, start, path, target, result):
        if target == 0:
            result.append(path)
            return 
        if target < 0:
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            self._combine(nums, i+1, path + [nums[i]], target-nums[i], result)
