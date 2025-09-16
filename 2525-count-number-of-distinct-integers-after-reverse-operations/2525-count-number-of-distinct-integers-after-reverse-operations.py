class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        s = set(nums)
        for x in nums:
            s.add(int(str(x)[::-1]))
        return len(s)