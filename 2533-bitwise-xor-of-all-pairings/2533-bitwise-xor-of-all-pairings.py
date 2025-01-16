class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        c1 = len(nums1)
        c2 = len(nums2)
        x1 = 0
        x2 = 0
        if c1 % 2 != 0:
            for i in nums2:
                x2 ^= i
        if c2 % 2 != 0:
            for i in nums1:
                x1 ^= i
        return x1 ^ x2        