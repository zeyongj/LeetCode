class Solution:
    def maxSum(self, nums, m, k):
        # Initialize the result variable to store the maximum sum
        res = 0
        
        # Initialize a variable to keep track of the sum of the current window
        window_sum = 0
        
        # Create a dictionary to store element frequencies within the current window
        element_freq = defaultdict(int)
        
        # Iterate through the first 'k' elements of the 'nums' list
        for i in range(k):
            # Update the frequency of the current element in the dictionary
            element_freq[nums[i]] += 1
            
            # Add the current element to the sum of the current window
            window_sum += nums[i]
        
        # Check if the dictionary has at least 'm' distinct elements for the initial window
        if len(element_freq) >= m:
            res = max(window_sum, res)  # Update the result if it's greater than the current result
        
        # Iterate from index 'k' to the end of the 'nums' list
        for i in range(k, len(nums)):
            # Remove the element that is no longer in the current window from the sum
            window_sum -= nums[i - k]
            
            # Update the frequency of the removed element in the dictionary
            element_freq[nums[i - k]] -= 1
            
            # If the element's frequency becomes 0, remove it from the dictionary
            if element_freq[nums[i - k]] == 0:
                del element_freq[nums[i - k]]
            
            # Update the frequency of the new element in the dictionary
            element_freq[nums[i]] += 1
            
            # Add the new element to the sum of the current window
            window_sum += nums[i]
            
            # Check if the dictionary has at least 'm' distinct elements for the current window
            if len(element_freq) >= m:
                res = max(window_sum, res)  # Update the result if it's greater than the current result
        
        # Return the maximum sum of almost unique subarrays
        return res