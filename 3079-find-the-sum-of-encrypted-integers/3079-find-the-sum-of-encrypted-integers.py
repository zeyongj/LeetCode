class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        output = 0
        for num in nums:
            m= str(num)
            output += int(max(m) * len(m))
        return output        