class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all elements to find xor_all which is the XOR of the two unique numbers
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        # Step 2: Find the rightmost set bit in xor_all
        rightmost_set_bit = xor_all & -xor_all
        
        # Step 3: Initialize the two unique numbers
        num1, num2 = 0, 0
        
        # Step 4: Split the numbers into two groups based on the rightmost set bit and XOR within each group
        for num in nums:
            if num & rightmost_set_bit:
                num1 ^= num
            else:
                num2 ^= num
        
        # Return the two unique numbers
        return [num1, num2]
