class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            # print(type(bin(i))) # <class 'str'>
            
            # if Number of Set Bits in Index(i) == k,, then Add Current Element in Ans. 
            if bin(i)[2:].count('1') == k:
                # In Returning value of bin(i),, there will be "0b",, at front of that string,, 
                # So, we are Slicing
                ans = ans + nums[i]

        return ans