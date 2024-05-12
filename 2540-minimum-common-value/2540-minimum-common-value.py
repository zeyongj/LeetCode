import numpy as np
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Two pointers:
        i, j = 0, 0
        len1, len2 = len(nums1), len(nums2)
        
        if len1 == 0 or len2 == 0:
            return -1
        
        while i < len1 and j < len2:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return -1
        
        
        
#         # Hash Map
#         set1 = set(nums1)
#         set2 = set(nums2)
        
#         num_count = {}
        
#         for num in set1:
#             num_count[num] = 1
        
#         for num in set2:
#             if num in num_count:
#                 num_count[num] += 1
#             else:
#                 num_count[num] = 1
        
#         minimum = np.inf
        
#         for num, count in num_count.items():
#             if count > 1:
#                 if num < minimum:
#                     minimum = num
        
#         return -1 if minimum == np.inf else minimum