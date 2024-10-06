class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
      for i in range(len(possible)):
        if possible[i]==0:
          possible[i] = -1
        else:
          continue  
      totSum = sum(possible)
      DanSum = 0
      BobSum = 0
      j = 0
      while j < len(possible)-1:
        DanSum += possible[j]
        BobSum = totSum - DanSum
        if DanSum > BobSum:
          return j+1
        j+=1
      return -1    
