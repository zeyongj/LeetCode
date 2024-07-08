import math
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        size = len(arr)
        
        target = math.floor(0.25 * size)
        
        numDict = {}
        
        for num in arr:
            if num not in numDict:
                numDict[num] = 1
            else:
                numDict[num] += 1

        
        for num,freq in numDict.items():
            if freq > target:
                return num