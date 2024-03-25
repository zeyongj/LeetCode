class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        size = len(s)
        
        if size == 0:
            return []
        
        left = 0
        right = size - 1
        
        self.recursion(s, left, right)
        
    def recursion(self, s: List[str], left: int, right: int) -> None:
        if left >= right:
            return []
        
        self.recursion(s, left+1, right-1)
        
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
    
        
#         # Stack method:
#         size = len(s)
        
#         if size == 0:
#             return []
        
#         temp = []
        
#         for c in s:
#             temp.append(c)
            
#         for i in range(size):
#             s[i] = temp.pop()
        
        
            
        
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
            
        