class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        size1 = len(word1)
        size2 = len(word2)
        outList = []
        
        if size1 == size2:
            for i in range(size1):
                outList.append(word1[i])
                outList.append(word2[i])
        elif size1 < size2:
            for i in range(size1):
                outList.append(word1[i])
                outList.append(word2[i])
            curr = size1
            while (curr < size2):
                outList.append(word2[curr])
                curr += 1
        else:
            for i in range(size2):
                outList.append(word1[i])
                outList.append(word2[i])
            curr = size2
            while (curr < size1):
                outList.append(word1[curr])
                curr += 1
        
        return "".join(outList)