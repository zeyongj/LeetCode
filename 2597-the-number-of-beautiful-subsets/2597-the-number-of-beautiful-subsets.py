class Solution:
    def dfs(self, nums: List[int], idx: int, k: int, mp: defaultdict) -> int:
        size = len(nums)
        if idx == size:
            return 1

        seen = 0
        if mp[nums[idx] - k] == 0 and mp[nums[idx] + k] == 0:
            mp[nums[idx]] += 1
            seen = self.dfs(nums, idx + 1, k, mp)
            mp[nums[idx]] -= 1
        
        # Depth first search, recursively
        notSeen = self.dfs(nums, idx + 1, k, mp)
        
        return seen + notSeen

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        num = self.dfs(nums, 0, k, mp)
        index = num - 1
        return index