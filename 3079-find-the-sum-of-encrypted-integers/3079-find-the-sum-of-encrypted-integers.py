class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        return sum(int(max(n)*len(n)) for n in map(str,nums)) 