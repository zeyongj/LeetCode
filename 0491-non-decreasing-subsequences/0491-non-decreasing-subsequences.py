class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(start, path):
            # If we have at least 2 elements, add to result
            if len(path) >= 2:
                result.append(path[:])
            
            # Use a set to track which values we've used at this level
            # to avoid duplicate subsequences
            used = set()
            
            for i in range(start, len(nums)):
                # Skip if we've already used this value at this level
                if nums[i] in used:
                    continue
                
                # Only add if path is empty or maintains non-decreasing order
                if not path or nums[i] >= path[-1]:
                    used.add(nums[i])
                    path.append(nums[i])
                    backtrack(i + 1, path)
                    path.pop()
        
        backtrack(0, [])
        return result