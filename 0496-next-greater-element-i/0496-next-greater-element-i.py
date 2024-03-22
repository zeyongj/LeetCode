class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        
        stack = []
        
        for num in nums2:
            stack.append(num)
            
        for num in nums1:
            temp = []
            isFound = False
            max = -1
            while (len(stack) != 0 and isFound == False):
                top = stack.pop()
                temp.append(top)
                if top > num:
                    max = top
                elif top == num:
                    isFound = True
                else:
                    continue
            output.append(max)
            
            while (len(temp) != 0):
                stack.append(temp.pop())
        
        return output
                
                    