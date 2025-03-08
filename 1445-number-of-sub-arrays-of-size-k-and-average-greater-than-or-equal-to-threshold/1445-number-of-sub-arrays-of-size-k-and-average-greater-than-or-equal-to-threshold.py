class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum,res=0,0
        for r in range(len(arr)):
            window_sum+=arr[r]
            if r>=k-1: 
                if window_sum/k>=threshold: res+=1
                window_sum-=arr[r-k+1]
        return res