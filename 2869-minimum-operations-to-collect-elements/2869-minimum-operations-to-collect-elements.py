class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        st = set()
        i = len(nums) - 1
        
        while len(st) < k:
            if nums[i] <= k:
                st.add(nums[i])
            i -= 1
            
        return len(nums) - i - 1