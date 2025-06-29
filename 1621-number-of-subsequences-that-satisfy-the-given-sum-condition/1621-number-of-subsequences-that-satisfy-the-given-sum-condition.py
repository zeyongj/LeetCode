class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD=10**9+7
        nums.sort()
        #[3,5,6,7]  if our min is 3 our max should be less thAN = target-min
        total=0
        def bs(arr,num):
            low=0
            high=len(arr)-1
            ans=0
            while low<=high:
                mid=(low+high)//2
                if arr[mid]<=num:
                    ans=mid
                    low=mid+1
                else:
                    high=mid-1
            return ans 
        for i,num in enumerate(nums):
            start_idx=i
            min_num=num
            max_num=target-num
            if min_num>max_num:
                continue
            end_idx=bs(nums,max_num)
            total=(total+pow(2,(end_idx-start_idx)))%MOD
        return total