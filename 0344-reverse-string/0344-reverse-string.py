class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        size = len(s)
        
        if size == 0:
            return []
        
        temp = []
        
        for c in s:
            temp.append(c)
            
        for i in range(size):
            s[i] = temp.pop()
        
        
            
        
        # Double pointer swap:
#         size = len(s)
        
#         if size == 0:
#             return []
        
#         left = 0
#         right = size - 1
        
#         while left < right:
#             temp = s[left]
#             s[left] = s[right]
#             s[right] = temp
#             left += 1
#             right -= 1
            
        