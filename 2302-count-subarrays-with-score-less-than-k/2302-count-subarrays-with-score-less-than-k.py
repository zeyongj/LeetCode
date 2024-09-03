class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pfx = [0] + list(accumulate(nums))
        res = 0
        for i in range(len(nums)):
            l, r = i, len(nums)
            while l < r:
                mid = (l+r+1)>>1
                if (pfx[mid]-pfx[i])*(mid-i) < k:
                    l = mid
                else: r = mid-1
            res+=l-i
        return res