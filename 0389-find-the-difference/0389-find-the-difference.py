class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sizeS = len(s)
        sizeT = len(t)
        
        if sizeS == 0:
            return t[0]
        
        occuranceList = [0] * 26
        
        for c in s:
            index = ord(c) - ord('a')
            occuranceList[index] -= 1
        
        for c in t:
            index = ord(c) - ord('a')
            occuranceList[index] += 1
        
        result = occuranceList.index(1)
        
        output = chr(result + ord('a'))
        
        return output