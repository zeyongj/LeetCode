class Solution:
    def maxSumRangeQuery(self, nums: List[int], req: List[List[int]]) -> int:
        n=len(nums)
        r=len(req)
        a=[0 for i in range(n)] 
        for i in range(r):
            a[req[i][0]]+=1
            if(req[i][1]<n-1):
                a[req[i][1]+1]-=1
        
        for i in range(n):
            if(i==0):
                continue
            a[i]+=a[i-1]

        a.sort()
        nums.sort()
        ans=0
        N=1e9 + 7
        for i in range(n-1,-1,-1):
            ans+=(a[i]*nums[i])%N
            ans%=N
        return int(ans%N)
