class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        xor = 0
        for i in nums:
            xor ^= i
        return len( nums ) % 2 == 0 or xor == 0