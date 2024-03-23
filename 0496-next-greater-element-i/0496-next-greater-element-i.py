class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        
        stack = []
        dictionary = {}
        
        for num in nums2:
            while (len(stack) > 0 and stack[-1] < num):
                temp = stack.pop()
                dictionary.update({temp:num})
            stack.append(num)
        
        # Remaining assigned -1
        while (len(stack) != 0):
            temp = stack.pop()
            dictionary.update({temp:-1})
        
        for num in nums1:
            output.append(dictionary.get(num))
        
        return output
        
#         output = []
        
#         stack = []
        
#         for num in nums2:
#             stack.append(num)
            
#         for num in nums1:
#             temp = []
#             isFound = False
#             max = -1
#             while (len(stack) != 0 and isFound == False):
#                 top = stack.pop()
#                 temp.append(top)
#                 if top > num:
#                     max = top
#                 elif top == num:
#                     isFound = True
#                 else:
#                     continue
#             output.append(max)
            
#             while (len(temp) != 0):
#                 stack.append(temp.pop())
        
#         return output
                
                    