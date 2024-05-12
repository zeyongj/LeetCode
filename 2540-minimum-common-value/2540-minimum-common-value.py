import numpy as np
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        set2 = set(nums2)
        
        num_count = {}
        
        for num in set1:
            num_count[num] = 1
        
        for num in set2:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        
        minimum = np.inf
        
        for num, count in num_count.items():
            if count > 1:
                if num < minimum:
                    minimum = num
        
        return -1 if minimum == np.inf else minimum