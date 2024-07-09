class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for num in nums:
            if nums[ans] < num:
                ans += 1
        return ans