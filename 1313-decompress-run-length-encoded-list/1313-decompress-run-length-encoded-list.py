class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        generated = []
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i+1]
            generated += [val] * freq 
        return generated