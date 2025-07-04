class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        avg = set()
        while nums:
            a = max(nums)
            b = min(nums)
            nums.remove(a)
            nums.remove(b)
            avg.add((a+b)/2)
        return len(avg)