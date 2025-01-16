class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd = even = alt = 0
        prev_parity = nums[0] & 1
        
        for num in nums:
            curr_parity = num & 1
            if curr_parity:
                odd += 1
            else:
                even += 1
            
            if curr_parity == prev_parity:
                alt += 1
                prev_parity ^= 1
        
        return max(odd, even, alt)