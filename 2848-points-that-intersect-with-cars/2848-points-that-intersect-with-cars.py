class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        seen = set()
        
        for a, b in nums:
            for i in range(a, b+1):
                seen.add(i)
        
        return len(seen)