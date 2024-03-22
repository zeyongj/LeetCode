class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        size = len(nums)
        
        if size == 0:
            return False
        
        numDict = {}
        
        for num in nums:
            if num not in numDict.keys():
                numDict[num] = 1
            else:
                val = numDict.get(num)
                val += 1
                numDict[num] = val
        
        occurances = numDict.values()
        
        for occurance in occurances:
            if occurance != 1:
                return True
        
        return False
        
#         for num in nums:
#             if num not in numDict.keys():
#                 numDict[num] = 1
#             else:
#                 return True
            
#         return False


        
#         mySet = set()
        
#         for num in nums:
#             mySet.add(num)
        
#         setLength = len(mySet)
        
#         if size == setLength:
#             return False
#         else:
#             return True
        
    
    