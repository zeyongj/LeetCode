class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        #i+ 1 >= n-i-1 (left >= right)
        #total = sum(nums)
        # one element to the right ( i (right) = total - left )
        total = sum(nums)
        c =  0
        left = 0 
        for  i in range( len(nums)  - 1 ) :
            left += nums[i]
            right = total - left 
            if left >= right :
                c += 1
        return c