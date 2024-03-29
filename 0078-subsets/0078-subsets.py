class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # DFS Method:
        
        res = []
        
        self.dfs(nums, res, 0, [])
        
        return res
        
    def dfs(self, nums: List[int], result: List[List[int]], index: int, subset: List[int]) -> None:
        temp = subset.copy()
        result.append(temp)
        
        if index == len(nums):
            return
        
        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, result, i+1, subset)
            subset.pop()
            
        
        
            
        
#         # Backtracking Method:
#         res = [[]]
        
#         size = len(nums)
        
#         for i in range (1, size + 1):
#             self.backtracking(nums, res, i, 0, [])
        
#         return res
    
#     def backtracking(self, nums: List[int], result: List[List[int]], length: int, index: int, subset: List[int]) -> None:
#         if len(subset) == length:
#             temp = subset.copy()
#             result.append(temp)
            
#         for i in range(index, len(nums)):
#             subset.append(nums[i])
#             self.backtracking(nums, result, length, i+1, subset)
#             subset.pop()
            
    
    
            
        
#         # Extension Method:
#         res = [[]]
        
#         for num in nums:
#             extension = [set + [num] for set in res]
#             res.extend(extension)
#             # temp = []
#             # for set in res:
#             #     extension = set + [num]
#             #     temp.append(extension)
#             # res.extend(temp)
        
#         return res