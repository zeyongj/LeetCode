class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        m=c=0
        for i in range(len(arr)):
            m=max(m,arr[i])
            if m==i:
                c+=1
        return c