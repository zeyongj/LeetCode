class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:

        # Number of Elements
        N  = len(nums)
      
        # Sort so that we can have partition
        nums.sort()

        # Trivial Case, all incremented OR all decremented
        score = nums[-1] - nums[0]

        # To store minimum score
        ans   = score

        # Check all N-1 Non-Trivial partitions/walls. 
        # Both sets will be non-empty   
        for divider in range(0, N-1):

            # Compute maximum and minimum after partitioning
            # Kudos! We only have two candidates for each
            maximumAfterDivision = max(nums[divider]    + k , nums[-1] - k)
            minimumAfterDivision = min(nums[divider+1]  - k , nums[0]  + k)

            # Score after dividing here
            score = maximumAfterDivision - minimumAfterDivision

            # ans will be minimum score
            ans = min(ans, score)
        
        # return answer
        return ans