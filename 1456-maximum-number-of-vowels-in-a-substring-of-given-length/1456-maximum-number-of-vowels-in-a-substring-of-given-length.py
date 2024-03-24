class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        size = len(s)
        
        if size == 0:
            return 0
        
        vowelSet = {"a", "e", "i", "o", "u"}
        
        left = 0
        right = k
        counter = 0
        
        for i in range(left,right):
            if s[i] in vowelSet:
                counter += 1
        
        res = counter
    
        while (right < size):
            if s[left] in vowelSet:
                counter -= 1
            left += 1
            if s[right] in vowelSet:
                counter += 1
            right += 1
            res = max(res,counter)
        
        return res
            
        
        
            