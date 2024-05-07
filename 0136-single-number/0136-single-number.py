class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # Xor Method - Time Complexity: O(n), Space Complexity: O(1)
        ans = 0
        
        for num in nums:
            ans = ans ^ num # xor property: x^x = 0 -> only single number remains, others are cancelled
        
        return ans
    
        # HashMap Mathod - Time Complexity: O(n), Space Complexity: O(n)
        
#         mapping = {}
        
#         for num in nums:
#             if num in mapping.keys():
#                 mapping[num] += 1
#             else:
#                 mapping[num] = 1
        
#         for num, occur in mapping.items():
#             if occur == 1:
#                 return num

    
                
        