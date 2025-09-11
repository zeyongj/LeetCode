class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        # Initialize an empty list to store the result subsequence
        minSubSequence = []
        
        # Sort the array in non-increasing order
        nums.sort(reverse=True)
        
        # Calculate the total sum of the array
        totalSum = sum(nums)
        
        # Initialize current sum of the subsequence
        currentSum = 0
        
        # Iterate through sorted array to construct the subsequence
        for num in nums:
            totalSum -= num  # Subtract the current number from total sum
            currentSum += num  # Add the current number to current sum
            minSubSequence.append(num)  # Add current number to subsequence
            
            # Check if current sum of subsequence > sum of remaining elements
            if currentSum > totalSum:
                return minSubSequence  # Return the subsequence
        
        return minSubSequence  # Return the subsequence if no conditions met